#!/usr/bin/env python3

import datetime
import os.path
import requests
import pprint
import io
import json
from zoneinfo import ZoneInfo

import git

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaIoBaseDownload


# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly',
          'https://www.googleapis.com/auth/drive.readonly']

def download_file(service, file_id, local_fd):
  """Download a Drive file's content to the local filesystem.

  Args:
    service: Drive API Service instance.
    file_id: ID of the Drive file that will downloaded.
    local_fd: io.Base or file object, the stream that the Drive file's
        contents will be written to.
  """
  request = service.files().get_media(fileId=file_id)
  fh = io.FileIO(local_fd, 'wb')
  downloader = MediaIoBaseDownload(fh, request)
  done = False
  while done is False:
      status, done = downloader.next_chunk()

def main():
    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    try:
        calendar_service = build('calendar', 'v3', credentials=creds)
        drive_service = build('drive', 'v3', credentials=creds)

        repo = git.Repo('.', search_parent_directories=True)
        events_json_file_path = os.path.join(repo.working_tree_dir, 'data', 'event_data.json')
        events_image_file_path = os.path.join(repo.working_tree_dir, 'src', 'lib', 'assets', 'images', 'events')

        # Call the Calendar API
        now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time
        events_result = calendar_service.events().list(calendarId='primary', timeMin=now,
                                              maxResults=20, singleEvents=True,
                                              orderBy='startTime').execute()
        events = events_result.get('items', [])

        if not events:
            return
        # Prints the start and name of the next 10 events
        # only public events
        # for some reason the "default" color means that colorId is not set -> those are the public events
        events = [ e for e in events if 'visibility' in e and e['visibility'] == 'public' or not 'colorId' in e ]
        events_data = []
        for event in events:
          event_data = {}
          # download attachments
          if 'attachments' in event:
            file_id = event['attachments'][0]['fileId']
            file_name = event['attachments'][0]['title']
            store_path = os.path.join(events_image_file_path, file_id + '_' + file_name)
            download_file(drive_service, file_id, store_path)
            event_data['image'] = file_id + '_' + file_name
            # lstrip <html-blob> from description
          if 'description' in event:
            event_data['description'] = event['description'].lstrip('<html-blob>')
          else:
            event_data['description'] = ''

          event_data['title'] = event['summary']
          event_data['begin'] = event['start']['dateTime'].rstrip('Z')
          event_data['end'] = event['end']['dateTime'].rstrip('Z')
          events_data.append(event_data)
          
        jsonevents = []
        with open(events_json_file_path, 'r') as f:
          # load existing events
          jsonevents = json.load(f)
          # remove all future events
        #pprint.pprint(jsonevents)
        jsonevents = [ e for e in jsonevents if datetime.datetime.fromisoformat(e['begin']) < datetime.datetime.now(ZoneInfo('Europe/Berlin')) ]
        # replace with new events from API
        jsonevents = jsonevents + events_data
        # serialize json to file
        with open(events_json_file_path, 'w') as f:
          json.dump(jsonevents, f, sort_keys=True, indent=4)

    except HttpError as error:
        print('An error occurred: %s' % error)
    file_id = '1RrnChjsKwT-GWl5E0MlkOXoXgUDyoB9g'
    drive_service = build('drive', 'v3', credentials=creds)

if __name__ == '__main__':
    main()

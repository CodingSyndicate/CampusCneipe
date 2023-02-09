import events_data from '$data/event_data.json';
import { base } from '$app/paths';

export function get_events({upcoming=true, count=7} = {}) {
  let events = events_data;
  events = events.map((event) => {
    if (typeof event.begin == "string") {
      event.begin_date = Date.parse(event.begin);
      if (event.begin.substr(event.begin.length - 6, 1) != "+")
      {
	let options = {
	  weekday: 'long',
	  year: 'numeric',
	  month: 'numeric',
	  day: 'numeric',
	  timeZone: 'Europe/Berlin'
	};
	event.begin_string = new Intl.DateTimeFormat('de-DE', options).format(event.begin_date);
      } else {
	let options = {
	  weekday: 'long',
	  year: 'numeric',
	  month: 'numeric',
	  day: 'numeric',
	  hour: 'numeric',
	  minute: 'numeric',
	  timeZone: 'Europe/Berlin'
	};
	event.begin_string = new Intl.DateTimeFormat('de-DE', options).format(event.begin_date);
      }
    }
    if (!event.image) {
      event.image = 'default.png';
    }
    return event;
  });
  let six_h_milliseconds = 1000 * 60 * 60 * 6;
  let cutoff = new Date().getTime() - six_h_milliseconds;
  let display_events;
  if (upcoming) {
    events.sort((a, b) => {
      if (a.begin_date < b.begin_date) return -1;
      else return 1;
    });
    display_events = events.filter(e => e.begin_date - cutoff >= 0);
  } else {
    // opposite order
    events.sort((a, b) => {
      if (a.begin_date > b.begin_date) return -1;
      else return 1;
    });
    display_events = events.filter(e => e.begin_date - cutoff < 0);
  }
  display_events = display_events.slice(0, count);
  return display_events;
}


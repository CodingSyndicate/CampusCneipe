import notices from '$data/notices.json';
import { get_events } from "$lib/server/events.js";

function convert_date(date_string) {
  options = {
    year: '2-digit',
    month: 'numeric',
    day: 'numeric',
    timeZone: 'Europe/Berlin'
  };
  return new Intl.DateTimeFormat('de-DE', options).format(date_string);
}

export async function load({ params }) {
  for (let notice in notices) {
    notices[notice].date_display_from = Date.parse(notices[notice].display_from)
    notices[notice].date_display_until = Date.parse(notices[notice].display_until)
  }
  let now = new Date().getTime();
  notices.sort((a, b) => {
    if (a.date_display_from < b.date_display_until) return -1;
    else return 1;
  });
  let filtered_notices = notices.filter(n => n.date_display_from < now && n.date_display_until > now);
  return {
    notices: filtered_notices,
    events: get_events({upcoming: true, count: 3})
  };
}

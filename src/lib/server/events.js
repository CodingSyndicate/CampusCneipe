import events from '$data/event_data.json';

export function get_events({upcoming=true, count=7} = {}) {
  for (let event in events) {
    if (typeof events[event].begin == "string") {
      events[event].begin = Date.parse(events[event].begin);
    }
  }
  let six_h_milliseconds = 1000 * 60 * 60 * 6;
  let cutoff = new Date().getTime() - six_h_milliseconds;
  let display_events;
  //export let display_events = [];
  if (upcoming) {
    events.sort((a, b) => {
      if (a.begin < b.begin) return -1;
      else return 1;
    });
    display_events = events.filter(e => e.begin - cutoff >= 0);
  } else {
    // opposite order
    events.sort((a, b) => {
      if (a.begin > b.begin) return -1;
      else return 1;
    });
    display_events = events.filter(e => e.begin - cutoff < 0);
  }
  display_events = display_events.slice(0, count);
  return display_events;
}

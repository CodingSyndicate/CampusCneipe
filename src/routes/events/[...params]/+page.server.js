import { get_events } from '$lib/server/events.js';
export async function load({ params }) {
  let ret = {}
  if (params.params == '') {
    ret.title = "Kommende Events"
    ret.button_href = "old/"
    ret.button_text = "Vergangene Veranstaltungen"
    ret.events = get_events();
  }else if (params.params.split('/')[0] == 'old') {
    ret.title = "Vergangene Events"
    ret.button_href = "../"
    ret.button_text = "Kommende Veranstaltungen"
    ret.events = get_events({upcoming: false, count: 20});
  }
  return ret;
}

<script>
  import events from '$data/event_data.json';
  import EventPreview from './EventPreview.svelte';

  export let count = 7;
  export let upcoming = true;
  for (let event in events) {
    if (typeof events[event].begin == "string") {
      events[event].begin = Date.parse(events[event].begin);
    }
  }

  let day_milliseconds = 1000 * 60 * 60 * 24;
  let cutoff = new Date().getTime() - day_milliseconds;
  export let display_events = [];
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
</script>

{#each display_events as event, i}
  {#if i % 2 == 0}
    <EventPreview {event} textRight={false} />
  {:else}
    <EventPreview {event} textRight={true} />
  {/if}
{/each}

<script>  
  import EventPreview from './EventPreview.svelte';
  export let events;

  events.forEach(event => {
    if(Array.isArray(event.date)) {
      event.date.forEach(date => {
	var new_event = event;
	new_event.date = date;
	events.push(new_event);
      })
    }
  });
  for (let event in events) {
    if (typeof events[event].date == "string") {
      events[event].date = Date.parse(events[event].date);
    }
  }
  events.sort((a, b) => {
    if (a.date < b.date) return -1;
    else return 1;
  });
  let day_milliseconds = 1000 * 60 * 60 * 24;
  let cutoff = new Date().getTime() - day_milliseconds;
</script>

<div class="rowContainer">
  {#each events as event}
    {#if event.date - cutoff >= 0}
      {@debug event}
    <EventPreview {event} />
  {/if}
  {/each}
</div>

<style>
	.rowContainer {
		min-height: 660px;
		width: 100%;
		background-color: #24292d;
		display: flex;
		flex-direction: row;
		align-items: center;
		justify-content: space-evenly;
		flex-wrap: wrap;
	}
	@media (max-width: 992px) {
		.rowContainer {
			flex-direction: column;
			height: auto;
		}
	}
</style>

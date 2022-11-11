<script>
	import events from '$data/event_data.json';
	import EventPreview from './EventPreview.svelte';

	const count = 7;
	for (let event in events) {
		if (typeof events[event].begin == 'string') {
			events[event].begin = Date.parse(events[event].begin);
		}
	}

	events.sort((a, b) => {
		if (a.begin < b.begin) return -1;
		else return 1;
	});
	const day_milliseconds = 1000 * 60 * 60 * 24;
	let cutoff = new Date().getTime() - day_milliseconds;
</script>

{#each events as event}
	{#if event.begin - cutoff >= 0}
		<EventPreview {event} />
	{/if}
{/each}

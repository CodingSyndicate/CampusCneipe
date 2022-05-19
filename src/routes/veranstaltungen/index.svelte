<script>
	import { events, wochenprogramm } from '$lib/data/events';

	import EventCardList from '$lib/EventCardList.svelte';
	import { Container } from 'svelte-chota';
</script>

<svelte:head>
	<title>Veranstaltungen | CampusCneipe</title>
	<meta name="description" content="Alle Veranstaltungen der Campus Cneipe" />
</svelte:head>

<div class="is-full-screen">
	<Container>
		<h1>Veranstaltungen</h1>
		<EventCardList title="Wochenprogramm" events={wochenprogramm} />

		<EventCardList title="Kommende Events" events={events.filter((event) => event.date >= new Date())} />
		<EventCardList title="Vergangene Events" events={events.filter((event) => event.date < new Date())} />
	</Container>
</div>

<script>
	import { events, wochenprogramm } from '$lib/data/events';

	import EventCardList from '$lib/EventCardList.svelte';
	import { Container } from 'svelte-chota';
</script>

<svelte:head>
	<title>Veranstaltungen | CampusCneipe</title>
	<meta name="description" content="Alle Veranstaltungen der Campus Cneipe" />
	<meta property="og:title" content="Veranstaltungen der Campus Cneipe" />
	<meta property="og:image" content="https://www.c2.tum.de/images/Hintergrundbild.jpg" />
	<meta property="og:url" content="https://www.c2.tum.de/veranstaltungen" />
	<meta property="og:site_name" content="Veranstaltungen der Campus Cneipe" />
	<meta property="og:description" content="Alle Veranstaltungen der Campus Cneipe" />
</svelte:head>

<div class="is-full-screen">
	<Container>
		<h1>Veranstaltungen</h1>
		<EventCardList title="Wochenprogramm" events={wochenprogramm} />

		<EventCardList title="Kommende Events" events={events.filter((event) => event.date >= new Date())} />
		<EventCardList title="Vergangene Events" events={events.filter((event) => event.date < new Date())} />
	</Container>
</div>

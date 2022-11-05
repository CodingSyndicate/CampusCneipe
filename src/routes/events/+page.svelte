<script>
	import Card from '$lib/Cards/Card.svelte';
	import TitelSeite from '$lib/Cards/TitelSeite.svelte';
	import EventPreviewList from '$lib/Events/EventPreviewList.svelte';
</script>

<svelte:head>
	<title>Events | CampusCneipe</title>
	<meta name="description" content="Alle Events der Campus Cneipe" />
	<meta property="og:title" content="Events der Campus Cneipe" />
	<meta property="og:image" content="https://www.c2.tum.de/images/Hintergrundbild.jpg" />
	<meta property="og:url" content="https://www.c2.tum.de/events" />
	<meta property="og:site_name" content="Events der Campus Cneipe" />
	<meta property="og:description" content="Alle Events der Campus Cneipe" />
</svelte:head>

<TitelSeite
	title="Events"
	subtitle="Veranstaltungen in der C2"
	full={false}
	middle={false}
	image="/images/events/event.JPG"
	imagePosition="center"
/>

<EventPreviewList />


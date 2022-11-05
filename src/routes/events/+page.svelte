<script>
	import Card from '$lib/Cards/Card.svelte';
	import TitelSeite from '$lib/Cards/TitelSeite.svelte';
	import EventPreviewList from '$lib/Events/EventPreviewList.svelte';
	import events from '$data/events.json';
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

<Card
	contentRight={false}
	sideImageHalf={true}
	title="Reopening Party WS 2022"
	subtitle="AM 24.10.2022 UM 15:00 UHR"
	bigImage="/images/events/events/reopening-ws22/reopeningws22.png"
>
	<p>Die Campus Cneipe feiert ihr Semester Reopening am 24.10.2022 um 15:00 Uhr.<br />Es gibt:</p>
	<ul>
		<li>130L Freibier!</li>
		<li>Überraschungsgast: TUM Präsident Hofmann</li>
		<li>Catering vom StuCafé</li>
		<li>Beerpong & Flunkyball</li>
	</ul>
	<p>Zeitplan</p>
	<ul>
		<li>15:00 Opening</li>
		<li>16:00 First 50L Free Beer</li>
		<li>17:00 Catering</li>
		<li>17:40 Official start with speech</li>
		<li>18:00 O'zapft is!</li>
	</ul>
	<p>Kommt vorbei! Wir freuen uns auf Euch!</p>
</Card>

<EventPreviewList {events} />

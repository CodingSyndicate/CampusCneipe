<script>
	import EventPreviewList from '$lib/Events/EventPreviewList.svelte';
	import DetailedCard from '$lib/Cards/DetailedCard.svelte';
	import TitelSeite from '$lib/Cards/TitelSeite.svelte';

	import Oeffnungszeiten from './Oeffnungszeiten.svelte';
	import Anfahrt from './anfahrt.svelte';
</script>

<svelte:head>
	<title>Die Campus Cneipe</title>
	<meta
		name="description"
		content="Die Campus Cneipe, eine studentische Kneipe der Technischen Universität München in Garching, bietet kostengünstige Getränke und Speisen an, sowie ein wöchentliches Pubquiz."
	/>
	<meta property="og:title" content="Die Campus Cneipe" />
	<meta property="og:image" content="https://www.c2.tum.de/images/Hintergrundbild.jpg" />
	<meta property="og:url" content="https://www.c2.tum.de/" />
	<meta property="og:site_name" content="Die Campus Cneipe" />
	<meta
		property="og:description"
		content="Die Campus Cneipe ist eine studentische Kneipe der Technischen Universität München in Garching."
	/>
</svelte:head>

<TitelSeite
	title="Die Campus Cneipe"
	subtitle="<p>am Forschungszentrum Garching<br>von Studenten/Studentinnen für Alle</p>"
	full={true}
	image="/images/2-2.png"
/>
<DetailedCard
	title="Die Cneipe am Campus Garching"
	subtitle="Mit studentischen Preisen"
	smallImageLeft="/images/4.JPG"
	smallImageRight="/images/5.JPG"
	bigImage="/images/3-1.png"
	text="Die Campus Cneipe sorgt seit der Gründung 2005 für Freizeitaktivitäten die den Campus Garching mit Studentenleben füllen. Geleitet, versorgt und am Laufen gehalten wird sie seit je her von TUM Studenten und Ehemaligen. 2020 in der neuen Mensa neugegründet erfindet sich die Campus Cneipe mit einem neuen Vorstand und vieler neuer Vereinsmitglieder neu. In Kooperation mit den Fachschaften, Studentenwerk und anderen Vereinen finden laufend erfolgreiche Veranstaltungen statt.
	Das Angebot an unterschiedlichen Bieren, Speisen und Cocktails ist mitgewachsen und so gibt es einige Neuigkeiten auszuprobieren. Schaut gerne mal rein!"
	buttonLink="/karte"
	buttonText="Karte öffnen"
	sideImageThird={true}
/>

<Oeffnungszeiten />

<Anfahrt />

<EventPreviewList />

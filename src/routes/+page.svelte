<script>
  import { base } from '$app/paths';
  import EventPreviewList from '$lib/Events/EventPreviewList.svelte';
  import DetailedCard from '$lib/Cards/DetailedCard.svelte';
  import TitelSeite from '$lib/Cards/TitelSeite.svelte';
  
  import Oeffnungszeiten from './Oeffnungszeiten.svelte';
  import Anfahrt from './anfahrt.svelte';

  import TitelImg from "$lib/assets/images/2-2.png";
  import CocktailImg1 from "$lib/assets/images/4.jpg";
  import CocktailImg2 from "$lib/assets/images/5.jpg";
  import MassImg from "$lib/assets/images/3-1.png";
  export let data;
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
	title="Campus Cneipe"
	subtitle="<p>am Forschungszentrum Garching<br>von Studenten/Studentinnen für Alle</p>"
	full={true}
	image={TitelImg}
  />
{#await data.notices then notes}
  <Oeffnungszeiten notices={notes} />
{/await}
<DetailedCard
	title="Die Cneipe am Campus Garching"
	subtitle="Mit studentischen Preisen"
	smallImageLeft={CocktailImg1}
	smallImageRight={CocktailImg2}
	bigImage={MassImg}
	text="Die Campus Cneipe sorgt seit der Gründung 2005 für Freizeitaktivitäten die den Campus Garching mit Studentenleben füllen. Geleitet, versorgt und am Laufen gehalten wird sie seit je her von TUM Studenten und Ehemaligen. 2020 in der neuen Mensa neugegründet erfindet sich die Campus Cneipe mit einem neuen Vorstand und vieler neuer Vereinsmitglieder neu. In Kooperation mit den Fachschaften, Studentenwerk und anderen Vereinen finden laufend erfolgreiche Veranstaltungen statt.
	Das Angebot an unterschiedlichen Bieren, Speisen und Cocktails ist mitgewachsen und so gibt es einige Neuigkeiten auszuprobieren. Schaut gerne mal rein!"
	buttonLink="/karte"
	buttonText="Karte öffnen"
	sideImageThird={true}
/>

<Anfahrt />

<hr />
{#await data.events then events}
  <EventPreviewList display_events={events} />
{/await}

<div class="text-center mt-5">
<a href="{ base }/events/">
  <button type="button" class="btn btn-primary">
    mehr Events
  </button>
</a>
</div>
<style>
  	hr {
		width: 66%;
		height: 2px;
		background-color: var(--bs-primary);
		opacity: 1;
		padding: 0;
		margin: auto;
		margin-top: 20px;
		margin-bottom: 20px;
		border: none;
	}

</style>

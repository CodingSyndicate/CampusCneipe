<script>
	import Card from '$lib/Cards/Card.svelte';
	import TitelSeite from '$lib/Cards/TitelSeite.svelte';
  import EventPreviewList from '$lib/Events/EventPreviewList.svelte';
  import TitelImage from "$lib/assets/images/events/event.jpg";
</script>

<svelte:head>
	<title>Vergangene Events | CampusCneipe</title>
	<meta name="description" content="Vergangene Events der Campus Cneipe" />
	<meta property="og:title" content="Events der Campus Cneipe" />
	<meta property="og:image" content="https://www.c2.tum.de/images/Hintergrundbild.jpg" />
	<meta property="og:url" content="https://www.c2.tum.de/events" />
	<meta property="og:site_name" content="Events der Campus Cneipe" />
	<meta property="og:description" content="Alle Events der Campus Cneipe" />
</svelte:head>

<TitelSeite
  title="Vergangene Events"
  subtitle='Vergangene Veranstaltungen in der C2
	    <div class="buttons">
	      <a href="../">
		<button type="button" class="btn btn-primary">
		  Kommende Veranstaltungen
		</button>
	    </a></div>'
	full={false}
	middle={false}
	image={TitelImage}
	imagePosition="center"
/>

<EventPreviewList upcoming={false} />


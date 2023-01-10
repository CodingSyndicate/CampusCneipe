<script>
  import TitelSeite from '$lib/Cards/TitelSeite.svelte';
  import EventPreviewList from '$lib/Events/EventPreviewList.svelte';
  import TitelImage from "$lib/assets/images/events/event.jpg";
  export let data;
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
{#await data then dat}
<TitelSeite
	title={dat.title}
	subtitle='Veranstaltungen in der C2<br>	<div class="buttons">
		  <a href="{dat.button_href}">
		    <button type="button" class="btn btn-primary">
		      {dat.button_text}
		    </button>
		  </a></div>'
	full={false}
	middle={false}
	image={TitelImage}
	imagePosition="center"
/>
{#key dat.events}
<EventPreviewList display_events={dat.events} />
{/key}
{/await}

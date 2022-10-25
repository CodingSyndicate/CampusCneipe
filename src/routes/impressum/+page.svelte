<script>
	import ImpressumNotice from './ImpressumNotice.svelte';
</script>

<svelte:head>
	<title>Impressum | CampusCneipe</title>
	<meta name="description" content="Impressum der Campus Cneipe" />
	<meta property="og:title" content="Impressum der Campus Cneipe" />
	<meta property="og:image" content="https://www.c2.tum.de/images/Hintergrundbild.jpg" />
	<meta property="og:url" content="https://www.c2.tum.de/impressum" />
	<meta property="og:site_name" content="Impressum der Campus Cneipe" />
	<meta property="og:description" content="Impressum der Campus Cneipe" />
</svelte:head>

<div class="container">
	<h1>Impressum</h1>
	<ImpressumNotice />
</div>

<style>
	h1 {
		font-size: 2.5rem;
		font-weight: 700;
		margin-bottom: 1rem;
		margin-top: 4rem;
	}
</style>

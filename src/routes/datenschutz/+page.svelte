<script>
	import PrivacyNotice from './PrivacyNotice.svelte';
</script>

<svelte:head>
	<title>Datenschutz | CampusCneipe</title>
	<meta name="description" content="Datenschutzerklärung der Campus Cneipe" />
	<meta property="og:title" content="Datenschutzerklärung der Campus Cneipe" />
	<meta property="og:image" content="https://www.c2.tum.de/images/Hintergrundbild.jpg" />
	<meta property="og:url" content="https://www.c2.tum.de/datenschutz" />
	<meta property="og:site_name" content="Datenschutzerklärung der Campus Cneipe" />
	<meta property="og:description" content="Datenschutzerklärung der Campus Cneipe" />
</svelte:head>

<div class="container">
	<h1>Datenschutzerklärung</h1>
	<PrivacyNotice />
</div>

<style>
	h1 {
		font-size: 2.5rem;
		font-weight: 700;
		margin-bottom: 1rem;
		margin-top: 4rem;
	}
</style>

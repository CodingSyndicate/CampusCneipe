<script>
	import ImpressumNotice from '$lib/Legal/ImpressumNotice.svelte';
	import { Container } from 'svelte-chota';
</script>

<svelte:head>
	<title>Impressum | CampusCneipe</title>
	<meta name="description" content="Impressum der Campus Cneipe" />
</svelte:head>

<div class="is-full-screen">
	<Container>
		<h1>Impressum</h1>
		<ImpressumNotice />
	</Container>
</div>

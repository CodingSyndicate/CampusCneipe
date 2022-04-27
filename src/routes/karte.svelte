<script>
	import { Container } from 'svelte-chota';
</script>

<svelte:head>
	<title>Karte | CampusCneipe</title>
	<meta name="description" content="Karte aller Getränke und Speisen der Campus Cneipe" />
</svelte:head>

<div class="is-full-screen">
	<Container>
		<h1>Karte</h1>
	</Container>
	<iframe title="Karte" src="./karte.pdf#view=fitH" class="is-full-screen pdf" />
</div>

<style>
	.pdf {
		padding-left: 2rem;
		padding-right: 2rem;
	}
</style>

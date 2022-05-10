<script>
	import 'chota';
	import '../app.css';
	import Footer from '$lib/Layout/Footer.svelte';
	import Nav from '$lib/Layout/Nav.svelte';
</script>

<svelte:head>
	<meta property="og:type" content="website" />
	<meta property="og:locale" content="de_DE" />
</svelte:head>
<div>
	<Nav />
	<main>
		<slot />
	</main>
	<Footer />
</div>

<style>
	main {
		margin: 0;
	}
</style>

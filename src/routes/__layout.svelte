<script>
	import 'chota';
	import '../app.css';
	import Footer from '$lib/Layout/Footer.svelte';
	import Nav from '$lib/Layout/Nav.svelte';
	import { Container } from 'svelte-chota';
</script>

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

<!-- <script context="module">
	export async function load({ url }) {
		if (url.protocol === 'https:') {
			return {};
		}
		if (url.protocol === 'http:' && !url.hostname.startsWith('localhost')) {
			return {
				status: 301,
				redirect: 'https://www.c2.tum.de'
			};
		}
		return {};
	}
</script> -->
<script>
	import 'chota';
	import '../app.css';
	import Footer from '$lib/Layout/Footer.svelte';
	import Nav from '$lib/Layout/Nav.svelte';
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

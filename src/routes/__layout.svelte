<script>
	import 'chota';
	import Footer from '$lib/Layout/Footer.svelte';
	import Nav from '$lib/Layout/Nav.svelte';
	import { Container } from 'svelte-chota';
</script>

<Nav />

<Container>
	<div class="is-full-screen">
		<slot />
	</div>
</Container>

<Footer />

<script>
	import '../app.scss';
	export const prerender = true;
	export const ssr = false;
	import Footer from './Footer.svelte';
	import Nav from './Nav.svelte';
</script>

<svelte:head>
	<meta property="og:type" content="website" />
	<meta property="og:locale" content="de_DE" />
</svelte:head>

<div class="root container-fluid">
	<div class="row">
		<Nav />
		<main>
			<slot />
		</main>
		<Footer />
	</div>
</div>

<style>
	.root {
		width: 100vw;
		height: 100vh;
	}
	main {
		width: calc(100% - 320px);
		z-index: 0;
		min-height: 100vh;
		margin-left: 320px;
		padding: 0;
		font-family: 'Vollkorn', Lato, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto,
			'Helvetica Neue', Arial, sans-serif, 'Apple Color Emoji', 'Segoe UI Emoji', 'Segoe UI Symbol';
	}
	@media (max-width: 992px) {
		.row {
			flex-direction: column;
		}
		main {
			width: 100%;
			margin-left: 0;
			margin-top: 108px;
		}
	}
</style>

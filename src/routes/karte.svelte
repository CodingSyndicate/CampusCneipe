<script>
	import { browser } from '$app/env';

	import { Container } from 'svelte-chota';
	import { onMount } from 'svelte';

	let PDFViewer;

	onMount(async () => {
		PDFViewer = (await import("@fabiohvp/svelte-pdfjs")).default;
	})
</script>

<svelte:head>
	<title>Karte | CampusCneipe</title>
	<meta name="description" content="Karte aller Getränke und Speisen der Campus Cneipe" />
</svelte:head>

<div class="is-full-screen">
	<Container>
		<h1>Karte</h1>
	</Container>

	<PDFViewer src="/karte.pdf"></PDFViewer>
	<!-- <div class="outerpdf">
		<iframe title="Karte" src="/karte.pdf#zoom=FitH" class="is-full-screen pdf" scrolling="auto" type="application/pdf" width="100%" height="100%" />
	</div> -->
</div>

<style>
	.outerpdf {
		-webkit-overflow-scrolling: touch;
		overflow: auto;
	}
	.pdf {
		padding-left: 2rem;
		padding-right: 2rem;
	}
</style>

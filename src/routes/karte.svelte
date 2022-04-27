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
	<div class="outerpdf">
		<iframe
			title="Karte"
			src="https://drive.google.com/viewerng/viewer?embedded=true&url=https://www.c2.tum.de/karte.pdf#view=FitH"
			class="is-full-screen pdf"
			allowfullscreen
			frameborder="0"
			scrolling="auto"
			width="100%"
			height="100%"
		/>
	</div>
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

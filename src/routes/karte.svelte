<script>
	import { Container, Icon } from 'svelte-chota';
	import { mdiLoading } from '@mdi/js';

	let loading = true;
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
		{#if loading}
			<div class="spinner">
				<Icon src={mdiLoading} spin="1" size="2" />
			</div>
		{/if}
		<iframe
			title="Karte"
			src="https://drive.google.com/viewerng/viewer?embedded=true&url=https://www.c2.tum.de/karte.pdf#view=FitH"
			class="pdf is-full-screen"
			allowfullscreen
			frameborder="0"
			scrolling="auto"
			width="100%"
			height="100%"
			on:load={() => (loading = false)}
		/>
	</div>
</div>

<style>
	.spinner {
		display: flex;
		justify-content: center;
	}
	.outerpdf {
		-webkit-overflow-scrolling: touch;
		overflow: auto;
	}
	.pdf {
		padding-left: 2rem;
		padding-right: 2rem;
	}
</style>

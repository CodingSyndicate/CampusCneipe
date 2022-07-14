<script>
	import { goto } from '$app/navigation';

	import { Container, Tag, Button } from 'svelte-chota';
	let googleMapsAccepted = false;
	let innerWidth;
	let innerHeight;
</script>

<svelte:window bind:innerWidth bind:innerHeight />

<svelte:head>
	<title>Anfahrt | CampusCneipe</title>
	<meta name="description" content="Anfahrt zur Campus Cneipe" />
	<meta property="og:title" content="Anfahrt zur Campus Cneipe" />
	<meta property="og:image" content="https://www.c2.tum.de/images/Hintergrundbild.jpg" />
	<meta property="og:url" content="https://www.c2.tum.de/anfahrt" />
	<meta property="og:site_name" content="Anfahrt zur Campus Cneipe" />
	<meta property="og:description" content="Anfahrt zur Campus Cneipe" />
</svelte:head>

<div class="is-full-screen">
	<Container>
		<h1>Anfahrt</h1>
		<section>
			<h3>Google Maps Navigation</h3>
			{#if googleMapsAccepted}
				<iframe
					title="Anfahrt zur Campus Cneipe über Google Maps"
					src="https://www.google.com/maps/embed?pb=!1m28!1m12!1m3!1d1610.3112722950407!2d11.670865797218344!3d48.26652079580697!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!4m13!3e3!4m5!1s0x479e72ece78d321f%3A0xf8d2874f0eb7c24c!2sGarching-Forschungszentrum%2C%20Garching%20bei%20M%C3%BCnchen!3m2!1d48.265043299999995!2d11.6715693!4m5!1s0x479e7292ea3852a1%3A0xab73615c78d2ce12!2sCampus-Cneipe%20C2%2C%20Boltzmannstra%C3%9Fe%2019%2C%2085748%20Garching%20bei%20M%C3%BCnchen!3m2!1d48.2678406!2d11.6722871!5e0!3m2!1sde!2sde!4v1657822733861!5m2!1sde!2sde"
					width={innerWidth > 800 ? 800 : innerWidth}
					height={innerHeight > 600 ? 600 : innerHeight}
					style="border:0;"
					allowfullscreen=""
					loading="lazy"
					referrerpolicy="no-referrer-when-downgrade"
				/>
			{:else}
				<div>
					<Button primary on:click={() => (googleMapsAccepted = true)}>Accept Google Maps Terms of Use</Button>
				</div>
			{/if}
			<div>
				<Button primary on:click={() => goto('https://goo.gl/maps/2TZmUkNPbSJDpJw28')}>Open in Google Maps</Button>
			</div>
		</section>
	</Container>
</div>

<style>
	section {
		display: flex;
		flex-direction: column;
		align-items: center;
		justify-content: center;
	}
	section > * {
		margin: 1rem 0;
	}
</style>

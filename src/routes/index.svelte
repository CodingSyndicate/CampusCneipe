<script>
	import Reservierungstool from '$lib/Reservierung/Reservierungstool.svelte';
	import { wochenprogramm, events } from '$lib/data/events';
	import EventCardList from '$lib/EventCardList.svelte';
	import BeerAnimation from '$lib/BeerAnimation.svelte';
</script>

<svelte:head>
	<title>Die Campus Cneipe</title>
	<meta
		name="description"
		content="Die Campus Cneipe, eine studentische Kneipe der Technischen Universität München in Garching, bietet kostengünstige Getränke und Speisen an, sowie ein wöchentliches Pubquiz."
	/>
	<meta property="og:title" content="Die Campus Cneipe" />
	<meta property="og:image" content="https://www.c2.tum.de/images/Hintergrundbild.jpg" />
	<meta property="og:url" content="https://www.c2.tum.de/" />
	<meta property="og:site_name" content="Die Campus Cneipe" />
	<meta property="og:description" content="Die Campus Cneipe ist eine studentische Kneipe der Technischen Universität München in Garching." />
</svelte:head>

<div class="background">
	<div class="banner">
		<span>Boltzmannstraße 19, 85748 Garching b. München</span> <br />
		<span>Öffnungszeiten: Di-Fr 15 - 24 Uhr</span>
	</div>
	<div class="is-full-screen mycol">
		<!-- <Tag class="bg-error">An Fronleichnam (16.6.), am 17.6. sowie in der GESAMTEN Garnix Woche (21.6.-24.6.) hat die Campus Cneipe geschlossen.</Tag> -->
		<div class="content">
			<div class="meldungen">
				<BeerAnimation />
				<h1 class="c2">Die Campus Cneipe</h1>
				<BeerAnimation mirror={true} />
			</div>
			<Reservierungstool />
		</div>
	</div>
</div>

<EventCardList title="Wochenprogramm" events={wochenprogramm} />
<EventCardList title="Kommende Events" events={events.filter((event) => event.date >= new Date())} />

<style>
	.background {
		background-image: url('/images/Hintergrundbild.jpg');
		background-size: cover;
		background-color: rgba(77, 82, 86, 0.5);
		background-blend-mode: multiply;
	}
	.banner {
		text-align: center;
		display: flex;
		flex-direction: column;
		justify-content: center;
		align-items: center;
		padding: 1em;
		background-color: rgba(47, 4, 4, 0.8);
	}
	.mycol {
		display: flex;
		width: 100%;
		height: 100%;
		flex-direction: column;
		justify-content: center;
		align-items: center;
	}
	.content {
		margin-top: 10rem;
		width: 100%;
		height: 100%;
	}
	.meldungen {
		width: 100%;
		min-height: 40rem;
		display: flex;
		align-items: center;
		text-align: center;
		justify-content: center;
		flex-direction: row;
	}
	.c2 {
		font-size: 4em;
		font-weight: 700;
		text-decoration: none;
		text-transform: uppercase;
		color: var(--color-primary);
	}
	@media (max-width: 768px) {
		.background {
			background-position: 50%;
		}
		.meldungen {
			padding-top: 10rem;
		}
	}
</style>

<script>
	import Reservierungstool from '$lib/Reservierung/Reservierungstool.svelte';
	import { Tag } from 'svelte-chota';
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
		<Tag class="bg-error">An Fronleichnam (16.6.), am 17.6. sowie in der GESAMTEN Garnix Woche (21.6.-24.6.) hat die Campus Cneipe geschlossen.</Tag>
		<div class="content">
			<div class="meldungen">
				<h1 class="glitch" data-glitch="Die Campus Cneipe">Die Campus Cneipe</h1>
			</div>
			<Reservierungstool />
		</div>
	</div>
</div>

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
	}
	.glitch {
		font-size: 5.2em;
		font-weight: 700;
		text-decoration: none;
		text-transform: uppercase;
		position: relative;
		top: 50%;
		left: 50%;
		transform: translate(-50%, -50%);
		margin: 0;
		color: var(--color-primary);
		letter-spacing: 5px;
	}
	.glitch:before,
	.glitch:after {
		display: block;
		content: attr(data-glitch);
		text-transform: uppercase;
		position: absolute;
		top: 0;
		left: 0;
		height: 100%;
		width: 100%;
		opacity: 0.8;
	}
	.glitch:after {
		color: #f0f;
		z-index: -2;
	}
	.glitch:before {
		color: #0ff;
		z-index: -1;
	}
	.glitch:hover:before {
		animation: glitch 0.3s cubic-bezier(0.25, 0.46, 0.45, 0.94) both 5;
	}
	.glitch:hover:after {
		animation: glitch 0.3s cubic-bezier(0.25, 0.46, 0.45, 0.94) reverse both 5;
	}
	@media only screen and (max-width: 400px) {
		.glitch {
			font-size: 3em;
		}
	}
	@keyframes glitch {
		0% {
			transform: translate(0);
		}
		20% {
			transform: translate(-5px, 5px);
		}
		40% {
			transform: translate(-5px, -5px);
		}
		60% {
			transform: translate(5px, 5px);
		}
		80% {
			transform: translate(5px, -5px);
		}
		to {
			transform: translate(0);
		}
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

<script>
	import { Input, Button, Tag } from 'svelte-chota';

	// add zeros infront of number until it has at least 2 digits
	function pad(number) {
		return (number < 10 ? '0' : '') + number;
	}

	let date = new Date();
	let currentdate = date.getFullYear() + '-' + pad(date.getMonth() + 1) + '-' + pad(date.getDate());
	let currenttime = pad(date.getHours()) + ':' + pad(date.getMinutes());

	let reservationDate = currentdate;
	let reservationTime = currenttime;
	let reservationName = undefined;
	let reservationPersons = undefined;

	$: submitDisabled =
		reservationDate === null ||
		reservationTime === null ||
		reservationName === undefined ||
		reservationName === null ||
		reservationName.trim() === '' ||
		reservationPersons === undefined ||
		reservationPersons === null;

	async function submitReservation() {
		console.log('submitReservation');
		console.log('reservationDate: ' + reservationDate);
		console.log('reservationTime: ' + reservationTime);
		console.log('reservationName: ' + reservationName);
		console.log('reservationPersons: ' + reservationPersons);
	}
</script>

<svelte:head>
	<title>Die Campus Cneipe</title>
	<meta property="og:title" content="Die Campus Cneipe" />
	<meta property="og:url" content="https://c2.raiser.dev/" />
	<meta name="description" content="Future website of the Campus Cneipe @ Technical University of Munich" />
	<meta property="og:description" content="Future website of the Campus Cneipe @ Technical University of Munich" />
	<meta property="og:image" content="https://c2.raiser.dev/favicon.png" />
</svelte:head>

<div class="background">
	<div class="banner">
		<span>Boltzmannstraße 19, 85748 Garching b. München</span> <br />
		<span>Öffnungszeiten: Di-Fr 15 - 24 Uhr</span> <br />
	</div>
	<div class="is-full-screen mycol">
		<div class="content">
			<div class="meldungen">
				<h1 class="glitch" data-glitch="Die Campus Cneipe">Die Campus Cneipe</h1>
			</div>
			<div class="tabletag">
				<p class="is-center"><Tag large>Tisch Reservieren</Tag></p>
			</div>
			<div class="reservierungstool">
				<p><Input placeholder="Your Name" bind:value={reservationName} /></p>
				<div class="spacer" />
				<p><Input type="time" bind:value={reservationTime} min="15:00" max="23:50" /></p>
				<div class="spacer" />
				<p><Input date bind:value={reservationDate} min={currentdate} /></p>
				<div class="spacer" />
				<p><Input number placeholder="2 Personen" bind:value={reservationPersons} min="1" max="10" /></p>
				<div class="spacer" />
				<p><Button primary bind:disabled={submitDisabled} on:click={submitReservation}>Reservieren</Button></p>
			</div>
		</div>
	</div>
</div>

<style>
	.tabletag {
		max-width: fit-content;
		margin: auto;
		transition: 0.3s;
	}
	.tabletag:hover {
		background-color: var(--color-primary);
	}
	.background {
		background-image: url('/Hintergrundbild.jpg');
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
	.reservierungstool {
		display: flex;
		flex-direction: row;
		justify-content: center;
		align-items: center;
		padding: 1em;
	}
	.spacer {
		height: 1em;
		width: 1em;
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
		min-width: 100vw;
		width: 100%;
		min-height: 40rem;
	}
	.glitch {
		font-size: 5.2em;
		font-weight: 700;
		text-decoration: none;
		text-transform: uppercase;
		position: absolute;
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
		.reservierungstool {
			flex-direction: column;
		}
		.background {
			background-position: 50%;
		}
	}
</style>

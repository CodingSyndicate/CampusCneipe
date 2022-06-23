<script>
	import { Input, Button, Tag, Icon } from 'svelte-chota';
	import { mdiLoading } from '@mdi/js';

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
	let reservationMail = undefined;

	let loading = false;
	let successfull = null;

	const validateEmail = (email) => {
		return String(email)
			.toLowerCase()
			.match(/^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/);
	};

	console.log(validateEmail('marvin@web.de'));

	$: submitDisabled =
		reservationDate === null ||
		reservationTime === null ||
		reservationName === undefined ||
		reservationName === null ||
		reservationName.trim() === '' ||
		reservationMail === undefined ||
		reservationMail === null ||
		reservationMail.trim() === '' ||
		validateEmail(reservationMail.trim()) === null ||
		reservationPersons === null ||
		reservationPersons === 'Personenzahl';

	async function submitReservation() {
		console.log('submitReservation');
		console.log('reservationDate: ' + reservationDate);
		console.log('reservationTime: ' + reservationTime);
		console.log('reservationName: ' + reservationName);
		console.log('reservationPersons: ' + reservationPersons);

		let day = new Date(reservationDate).toLocaleString('de-de', { weekday: 'long' });

		let string = `${day} ${reservationDate} ${reservationTime} ${reservationName} ${reservationPersons}`;
		loading = true;
		let response = await fetch(
			`https://www.c2.tum.de/reservierung.php?name=${reservationName}&mail=${reservationMail.trim()}&day=${day}&date=${reservationDate}&time=${reservationTime.replace(
				':',
				'%3A'
			)}&person=${reservationPersons}`,
			{
				method: 'GET',
				mode: 'no-cors', // no-cors, *cors, same-origin
				cache: 'no-cache', // *default, no-cache, reload, force-cache, only-if-cached
				credentials: 'same-origin', // include, *same-origin, omit
				redirect: 'follow', // manual, *follow, error
				referrerPolicy: 'same-origin' // no-referrer, *no-referrer-when-downgrade, origin, origin-when-cross-origin, same-origin, strict-origin, strict-origin-when-cross-origin, unsafe-url
			}
		);
		loading = false;
		if (response.status === 200) {
			successfull = true;
		} else {
			successfull = false;
		}
		console.log('reservation submitted', response);
	}
</script>

<div class="tabletag">
	<p class="is-center"><Tag large>Tisch Reservieren</Tag></p>
</div>
<div class="reservierungstool">
	<div class="reservierungstoolRow">
		<p class="nameInput"><Input placeholder="Your Name" bind:value={reservationName} /></p>
		<div class="spacer" />
		<p class="emailInput"><Input placeholder="Your Email" bind:value={reservationMail} /></p>
		<div class="spacer" />
	</div>
	<div class="reservierungstoolRow">
		<p><Input date bind:value={reservationDate} min={currentdate} /></p>
		<div class="spacer" />
		<p class="timeInput">
			<span class="tooltiptext">Öffnungszeiten: Di-Fr 15 - 24 Uhr</span>
			<Input type="time" bind:value={reservationTime} min="15:00" max="23:50" />
		</p>
		<div class="spacer" />
		<p>
			<select bind:value={reservationPersons}>
				<option disabled selected>Personenzahl</option>
				{#each Array.from({ length: 10 }, (_, i) => i + 1) as i}
					<option value={i}>{i} Personen</option>
				{/each}
			</select>
		</p>
		<div class="spacer" />
	</div>
	<p>
		{#if successfull != null}
			<Tag>
				{#if successfull}
					<span class="text-success">Reservierung erfolgt! ✅</span>
				{:else}
					<span class="text-error">Reservierung nicht möglich! ❌</span>
				{/if}
			</Tag>
		{:else}
			<Button primary bind:disabled={submitDisabled} on:click={submitReservation}>
				{#if loading}
					<Icon src={mdiLoading} spin="1" size="2" />
				{:else}
					Reservieren
				{/if}
			</Button>
		{/if}
	</p>
</div>
<span class="is-center mailhintbox">
	Andere Reservierungen an: &nbsp;
	<a class="mailhint" href="mailto:reservierungen@campus-cneipe.de"> reservierungen@campus-cneipe.de</a>
</span>

<style>
	select {
		width: 150px;
	}
	.tooltiptext {
		opacity: 0;
		position: absolute;
		margin-top: -3rem;
		margin-left: -7.5rem;
		transition: 0.3s;
		background-color: #333;
		border-radius: 5px;
		padding: 0.5rem;
	}
	.timeInput:hover > .tooltiptext {
		opacity: 1;
	}
	.tabletag {
		max-width: fit-content;
		margin: auto;
		transition: 0.3s;
	}
	.tabletag:hover {
		background-color: var(--color-primary);
	}
	.reservierungstool {
		display: flex;
		flex-direction: column;
		justify-content: center;
		align-items: center;
		padding: 1em 1em 0 1em;
	}
	.reservierungstoolRow {
		display: flex;
		flex-direction: row;
	}
	.spacer {
		height: 1em;
		width: 1em;
	}
	a {
		color: var(--font-color);
	}
	@media (max-width: 450px) {
		.reservierungstoolRow {
			flex-direction: column;
		}
	}
	@media (max-width: 768px) {
		.mailhintbox {
			display: flex;
			flex-direction: column;
		}
	}
</style>

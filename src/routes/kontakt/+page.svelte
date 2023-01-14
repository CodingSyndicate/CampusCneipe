<script>
	import TitelSeite from '$lib/Cards/TitelSeite.svelte';
	import { base } from '$app/paths';
  import KontaktImg from "$lib/assets/images/kontakt.jpg";
	let name;
	let email;
	let request;
	let message;
	let checked = false;

	$: disabled = !(name && email && request && message && checked);

	let submitted = false;

	async function submitForm(e) {
		e.preventDefault();
		if (disabled) return;
		if (!checked) return;
		checked = false;
		let res = await fetch(base + '/api/handle_form.php', {
			method: 'POST',
			headers: {
				'Content-Type': 'multipart/form-data'
			},
			redirect: 'follow',
			body: JSON.stringify({
				name,
				email,
				request: request.split('_')[1],
				requesttype: request.split('_')[0],
				message,
				challenge: '9'
			})
		});
		if (res.ok) {
			submitted = true;
		} else {
			alert(
				'Es ist ein Fehler aufgetreten. Bitte überprüfen Sie Ihre Eingabe oder versuchen Sie es später erneut.'
			);
		}
	}
</script>

<svelte:head>
	<title>Kontakt | CampusCneipe</title>
	<meta
		name="description"
		content="Kontaktiere die Campus Cneipe für Reservierungen, Veranstaltungen oder für Mitarbeit"
	/>
	<meta property="og:title" content="Kontakt zur Campus Cneipe" />
	<meta property="og:image" content="https://www.c2.tum.de/images/Hintergrundbild.jpg" />
	<meta property="og:url" content="https://www.c2.tum.de/kontakt" />
	<meta property="og:site_name" content="Kontakt zur Campus Cneipe" />
	<meta
		property="og:description"
		content="Kontaktiere die Campus Cneipe für Reservierungen, Veranstaltungen oder für Mitarbeit"
	/>
</svelte:head>

<TitelSeite
	title="Kontakt"
	subtitle="Kontaktiere uns für Reservierungen oder Veranstaltungen!"
	full={false}
	middle={false}
	image={KontaktImg}
	imagePosition="center"
/>

<div class="kontakt">
	<div class="contactInfos">
		<div class="contactInfoRow p-3">
			<img src="{base}/svg/place_white_24dp.svg" alt="Adresse" />
			<p>CampusCneipe C2<br />Boltzmannstraße 19,<br />85748 Garching bei München</p>
		</div>
		<div class="contactInfoRow p-3">
			<img src="{base}/svg/phone_white_24dp.svg" alt="Telefon" />
			<p><a href="tel:+498928914430"> +49 89 289 14430</a></p>
		</div>
		<div class="contactInfoRow p-3">
			<img src="{base}/svg/email_white_24dp.svg" alt="Email" />
			<p>
				Event Anfragen: <a href="mailto:event@campus-cneipe.de">event@campus-cneipe.de</a>
				<br />
				Sonstige Anfragen: <a href="mailto:info@campus-cneipe.de">info@campus-cneipe.de</a>
			</p>
		</div>
	</div>
	<form aria-disabled="true" on:submit={submitForm}>
		<div class="row">
			<div class="col">
				<label for="inputName" class="form-label">Dein Name</label>
				<input bind:value={name} type="text" class="form-control" id="inputName" />
			</div>
			<div class="col">
				<label for="inputEmail" class="form-label">Deine Email Adresse</label>
				<input
					bind:value={email}
					type="email"
					class="form-control"
					id="inputEmail"
					aria-describedby="emailHelp"
				/>
				<div id="emailHelp" class="form-text">Wir geben deine Email Adresse niemals weiter.</div>
			</div>
		</div>
		<div class="mb-3">
			<label for="anfragentyp" class="form-label">Du möchtest...</label>
			<select
				bind:value={request}
				id="anfragentyp"
				class="form-select"
				aria-label="Anfragentyp wählen"
			>
				<option selected value="I_Tischreservierung">
					einen Tisch zu den Öffnungszeiten reservieren
				</option>
				<option value="E_Veranstaltung planen">
					eine Veranstaltung zusammen mit der C2 durchführen
				</option>
				<option value="P_Bewerbung als Mitarbeiter">für die C2 arbeiten</option>
				<option value="I_Sonstiges">Sonstiges</option>
			</select>
		</div>
		<div class="mb-3">
			<label for="textarea" class="form-label">Details zu deiner Anfrage</label>
			<textarea bind:value={message} class="form-control" id="textarea" rows="8" />
		</div>
		<div class="mb-3 form-check">
			<input bind:value={checked} type="checkbox" class="form-check-input" id="exampleCheck1" />
			<label class="form-check-label" for="exampleCheck1">
				Ich stimme dem <a href="{base}/datenschutz">Datenschutzhinweis</a> zur Verarbeitung meiner Anfrage
				zu.
			</label>
		</div>
		{#if submitted}
			<p style="color: rgb(0,255,0);">Erfolgreich abgeschickt!</p>
		{:else}
			<button type="submit" class="btn btn-primary" {disabled}> Submit </button>
		{/if}
	</form>
</div>

<style>
	.kontakt {
		padding-top: 2rem;
		width: 100%;
		display: flex;
		flex-direction: row;
		justify-content: space-evenly;
	}
	.contactInfos {
		width: 33.3333%;
		display: flex;
		flex-direction: column;
		align-items: center;
	}
	.contactInfoRow {
		display: flex;
		width: 25rem;
		flex-direction: row;
		align-items: center;
		margin-bottom: 3rem;
	}
	.contactInfoRow > img {
		width: 2rem;
		height: 2rem;
		margin-right: 2rem;
	}
	.contactInfoRow > p {
		margin: 0;
	}
	form {
		width: 66.6666%;
		padding-left: 3%;
		padding-right: 3%;
	}
	label {
		color: #bfbfbf;
	}
	textarea {
		font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell,
			'Open Sans', 'Helvetica Neue', sans-serif;
	}
	@media (max-width: 992px) {
		.kontakt {
			flex-direction: column-reverse;
		}
		.contactInfos {
			width: 100%;
		}
		form {
			width: 100%;
			margin-bottom: 3rem;
		}
		.contactInfoRow {
			width: 100%;
		}
	}
</style>

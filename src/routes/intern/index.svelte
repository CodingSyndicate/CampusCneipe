<script>
	import JobList from '$lib/Jobs/JobList.svelte';
	import { Field, Input, Row, Col, Button } from 'svelte-chota';

	let username;
	let password;

	let loading = false;
	let error = false;
	function submit() {
		// Submit login credentials
	}
</script>

<svelte:head>
	<title>Intern | CampusCneipe</title>
	<meta name="description" content="Interner Bereich für Mitarbeiter" />
</svelte:head>

<Col>
	<Row class="is-center">
		<h1>Interner Bereich</h1>
	</Row>
	<Row class="is-horizontal-align">
		<Col class="pull-right">
			<div class="extern">
				<h2>Externe Tools:</h2>
				<a href="https://schichtplaner-online.de/auth/login">Schichtplanner</a>
				<a href="https://trello.com">Trello</a>
				<a href="https://sheets.google.com">Google Sheets</a>
			</div>
		</Col>
		<Col>
			<div class="spacerBox">
				<div class="spacer" />
			</div>
		</Col>
		<Col class="pull-left">
			<h2>Login</h2>
			<Field label="Username">
				<Input bind:value={username} placeholder="User" />
			</Field>

			<Field label="Password">
				<Input password bind:value={password} placeholder="Password" />
			</Field>
			<Button {loading} {error} submit on:click={submit}>Send form</Button>
		</Col>
	</Row>
	<Row class="is-horizontal-align">
		<JobList />
	</Row>
</Col>

<style>
	.spacerBox {
		width: 100%;
		height: 100%;
		display: flex;
		justify-content: center;
		align-items: center;
	}
	.spacer {
		width: 3px;
		height: 70%;
		background-color: gray;
	}
	.extern {
		display: flex;
		flex-direction: column;
	}
	a {
		font-size: 2rem;
	}
</style>

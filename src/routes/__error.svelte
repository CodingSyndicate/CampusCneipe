<script context="module">
	export function load({ error, status }) {
		return {
			props: { error, status }
		};
	}
</script>

<script>
	import { dev } from '$app/env';
	export let error, status;
	import { Tag } from 'svelte-chota';
</script>

<svelte:head>
	<title>Error {status} - Aurasky</title>
	<meta name="description" content="Error" />
</svelte:head>

<div class="errorContainer">
	<h1>Oh Nein! Das Fass ist leer!</h1>

	<Tag>Wenn der Fehler häufiger auftritt schreibe gerne ein Issue auf <a href="https://github.com/CodingSyndicate/CampusCneipe/issues/new">Github</a> und wir arbeiten daran!</Tag>

	<h4 class="text-error">Fehlercode: {status}</h4>
	<p>{error.message}</p>

	{#if dev && error.stack}
		<pre>{error.stack}</pre>
	{/if}
</div>

<style>
	.errorContainer {
		padding: 4rem;
	}
	h1,
	p {
		margin: 0 auto;
	}
	h1 {
		font-size: 2.8em;
		font-weight: 700;
		margin: 0 0 0.5em 0;
	}
	p {
		margin: 1em auto;
	}
	@media (min-width: 480px) {
		h1 {
			font-size: 4em;
		}
	}
</style>

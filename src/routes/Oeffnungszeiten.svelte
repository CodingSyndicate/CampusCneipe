<script>
	import opening_times from '$data/opening_times.json';
	import { goto } from '$app/navigation';
	import Card from '$lib/Cards/Card.svelte';
	let bigImage = '/images/7.jpg';
</script>

<Card
	title="ÖFFNUNGSZEITEN"
	subtitle="KOMMT NACH DER VORLESUNG VORBEI!"
	{bigImage}
	contentRight={true}
	sideImageHalf={true}
	small={true}
	darkBackground={true}
>
	<span>In der Vorlesungszeit:</span>
	<ul>
		{#each opening_times as time}
			<li>{time.day}: {time.open} - {time.close} Uhr</li>
		{/each}
	</ul>
	<p>
		Außerhalb der Vorlesungszeit haben wir für den regulären Betrieb geschlossen. Die Campus Cneipe
		kann aber weiterhin für private Veranstaltungen jeglicher Art gebucht werden.
	</p>
	<div class="buttons">
		<button type="button" class="btn btn-primary" on:click={() => goto('/kontakt')}>
			Tisch reservieren
		</button>
		&nbsp;
		<button type="button" class="btn btn-outline-primary" on:click={() => goto('/mieten')}>
			C2 Mieten
		</button>
	</div>
</Card>

<style>
	button {
		margin-top: 0.5rem;
	}
	p {
		margin-top: 2rem;
		margin-bottom: 2rem;
	}
</style>

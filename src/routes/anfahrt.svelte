<script>
	import { goto } from '$app/navigation';
	import Card from '$lib/Cards/Card.svelte';
	import bigImage from '$lib/assets/images/navigation.png';
</script>

<Card
	title="Anfahrt"
	subtitle="Kommt nach der Vorlesung vorbei!"
	{bigImage}
	contentRight={false}
	sideImageHalf={true}
	small={true}
>
	<p>
		Die Campus Cneipe ist 2020 in die neue Mensa umgezogen und befindet sich direkt am Eck zum
		Innenhof des neuen Gebäudekomplexes.
	</p>
	<span>Die neue Adresse lautet:</span>
	<pre>
Boltzmannstraße 19,
85748 Garching bei München</pre>
	<p>Oder schaut auf dem Navigator Eurer Wahl vorbei:</p>
	<div class="buttons">
		<button
			type="button"
			class="btn btn-primary"
			on:click={() => goto('https://goo.gl/maps/bpuBkS9SuhXq9exE6')}
		>
			Google Maps
		</button>
		&nbsp;
		<button
			type="button"
			class="btn btn-outline-primary"
			on:click={() =>
				goto('https://www.openstreetmap.org/?mlat=48.26790&mlon=11.67205#map=18/48.26790/11.67205')}
		>
			Open Street Maps
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
	pre {
		padding-left: 1rem;
	}
</style>

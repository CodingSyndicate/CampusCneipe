<script>
	import KartenKategorie from '$lib/Karte/KartenKategorie.svelte';
	import Hintergrundbilder from '$lib/Karte/Hintergrundbilder.png';
	import { karte } from '$lib/data/karte';
</script>

<svelte:head>
	<title>Karte | CampusCneipe</title>
	<meta name="description" content="Karte aller Getränke und Speisen der Campus Cneipe" />
	<meta property="og:title" content="Getränkekarte der Campus Cneipe" />
	<meta property="og:image" content="https://www.c2.tum.de/images/Hintergrundbild.jpg" />
	<meta property="og:url" content="https://www.c2.tum.de/karte" />
	<meta property="og:site_name" content="Getränkekarte der Campus Cneipe" />
	<meta property="og:description" content="Karte aller Getränke und Speisen der Campus Cneipe" />
</svelte:head>

<img class="background" src={Hintergrundbilder} alt="Bild der Cneipe" />

{#each karte as category, i}
	{#if i % 2 === 0}
		<KartenKategorie {category} />
	{:else}
		<KartenKategorie {category} otherside={true} />
	{/if}
{/each}

<style>
	.background {
		width: 100%;
		height: 100%;
		object-fit: contain;
	}
</style>

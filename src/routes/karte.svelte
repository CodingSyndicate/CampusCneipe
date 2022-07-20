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
<section>
	<h4>Allergene + Zusatzstoffe</h4>
	<div class="row">
		<div class="notice">
			1 Coffeinhaltig <br />
			2 Chininhaltig <br />
			3 Taurin <br />
			4 Farbstoff <br />
		</div>
		<div class="notice">
			5 Schalenfrüchte <br />
			6 Milch <br />
			7 Schwefeldioxid/Sulfite <br />
		</div>
	</div>
	<p class="priceNotice">Alle Preise in Euro inkl. MWSt.</p>
</section>

<style>
	.background {
		width: 100%;
		height: 100%;
		object-fit: contain;
	}
	h4 {
		margin-bottom: 0;
	}
	section {
		display: flex;
		flex-direction: column;
		align-items: center;
	}
	.notice {
		font-size: 0.8em;
		text-align: left;
		padding-left: 1em;
		padding-right: 1em;
	}
	.priceNotice {
		padding-top: 1em;
		text-align: center;
	}
</style>

<script>
	import menu from '$data/menu_data.json';
	import KartenKategorie from './KartenKategorie.svelte';
</script>

<div class="kartenContainer">
	{#each menu as kategorie}
		<KartenKategorie {kategorie} />
	{/each}
</div>

<style>
	.kartenContainer {
		display: flex;
		flex-direction: column;
	}
</style>

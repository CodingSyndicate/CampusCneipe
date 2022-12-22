<script>
	import menu from '$data/menu_data.json';
	import KartenKategorie from './KartenKategorie.svelte';
	import { Tabs, TabList, TabPanel, Tab } from '$lib/Tabs/tabs.js';
</script>

<div class="kartenContainer">
	<Tabs>
		<TabList>
			{#each menu.products as kategorie}
				<Tab widthDividor={menu.length}>{kategorie.name}</Tab>
			{/each}
		</TabList>

		{#each menu.products as kategorie}
			<TabPanel>
				<KartenKategorie {kategorie} />
			</TabPanel>
		{/each}
	</Tabs>
</div>

<style>
	.kartenContainer {
		display: flex;
		flex-direction: column;
	}
</style>

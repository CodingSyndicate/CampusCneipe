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

<ul start="0" class="list-group fs-6">
  {#each menu.footnote_data.Allergene as allergen}
      <li><sup>{allergen.key}</sup> {allergen.name}</li>
    {/each}
    {#each menu.footnote_data.Inhaltsstoffe as inhaltsstoff}
      <li><sup>{inhaltsstoff.key}</sup> {inhaltsstoff.name}</li>
  {/each}

</ul>

<style>
	.kartenContainer {
		display: flex;
		flex-direction: column;
	}
</style>

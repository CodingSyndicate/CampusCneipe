<script>
	import { base } from '$app/paths';
	import { Tabs, TabList, TabPanel, Tab } from '$lib/Tabs/tabs.js';
	import { replaceUmlauts } from '$lib/utils.js';
	import KartenProduct from './KartenProduct.svelte';
	export let kategorie;
</script>

<div class="kategorieContainer">
	<img
		class="kategorieImage"
		src={base + '/images/karte/' + replaceUmlauts(kategorie.name) + '.JPG'}
		alt={kategorie.name}
	/>
	<div class="kategorieContent">
		<h1>{kategorie.name}</h1>
		<Tabs>
			<TabList>
				{#each kategorie.childs.filter((el) => el.products.length > 0) as childCategory}
					<Tab>{childCategory.name}</Tab>
				{/each}
			</TabList>

			{#each kategorie.childs.filter((el) => el.products.length > 0) as childCategory}
				<TabPanel>
					{#each childCategory.products as product}
						<KartenProduct {product} />
					{/each}
				</TabPanel>
			{/each}
		</Tabs>
	</div>
</div>

<style>
	.kategorieContainer {
		display: flex;
		flex-direction: row;
		margin-bottom: 0.5rem;
	}
	.kategorieImage {
		width: 50%;
		height: auto;
	}
	.kategorieContent {
		width: 50%;
		display: flex;
		flex-direction: column;
		align-items: center;
		padding-top: 2rem;
	}
	@media (max-width: 992px) {
		.kategorieContainer {
			flex-direction: column-reverse;
			height: auto;
		}
		.kategorieImage {
			width: 100%;
			height: auto;
		}
		.kategorieContent {
			width: 100%;
		}
	}
	h1 {
		text-transform: uppercase;
	}
</style>

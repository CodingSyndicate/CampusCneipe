<script>
	import { base } from '$app/paths';
	import { Tabs, TabList, TabPanel, Tab } from '$lib/Tabs/tabs.js';
	import { replaceUmlauts } from '$lib/utils.js';
	import { Collapse } from 'bootstrap'; // Neccessary for bootstrap to work
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
		<div class="accordion accordion-flush" id="accordionFlushExample">
			{#each kategorie.childs.filter((el) => el.products.length > 0) as childCategory}
				<div class="accordion-item">
					<h2
						class="accordion-header"
						id="flush-{replaceUmlauts(childCategory.name).split(' ')[0]}"
					>
						<button
							class="accordion-button collapsed"
							type="button"
							data-bs-toggle="collapse"
							data-bs-target="#flush-{replaceUmlauts(childCategory.name).split(' ')[0]}"
							aria-expanded="false"
							aria-controls="flush-{replaceUmlauts(childCategory.name).split(' ')[0]}"
						>
							{childCategory.name}
						</button>
					</h2>
					<div
						id="flush-{replaceUmlauts(childCategory.name).split(' ')[0]}"
						class="accordion-collapse collapse"
						aria-labelledby="flush-{replaceUmlauts(childCategory.name).split(' ')[0]}"
						data-bs-parent="#accordionFlushExample"
					>
						<div class="accordion-body">
							{#each childCategory.products as product}
								<KartenProduct {product} />
							{/each}
						</div>
					</div>
				</div>
			{/each}
		</div>
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
	.accordion {
		width: 100%;
		height: 100%;
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

<script>
	import { base } from '$app/paths';
	import { Tabs, TabList, TabPanel, Tab } from '$lib/Tabs/tabs.js';
	import { replaceUmlauts } from '$lib/utils.js';
	import { Collapse } from 'bootstrap'; // Neccessary for bootstrap to work
	import KartenProduct from './KartenProduct.svelte';
	export let kategorie;

	function idParser(id) {
		return replaceUmlauts(id)
			.split(' ')
			.join('-')
			.split('/')
			.join('-')
			.split('&')
			.join('-')
			.replace(/[^a-zA-Z ]/g, '');
	}
</script>

<div class="kategorieContainer">
	<img
		class="kategorieImage"
		src={base + '/images/karte/' + replaceUmlauts(kategorie.name) + '.JPG'}
		alt={kategorie.name}
	/>
	<div class="kategorieContent">
		<div class="accordion accordion-flush" id="accordionExample">
			{#each kategorie.childs.filter((el) => el.products.length > 0) as childCategory}
				<div class="accordion-item">
					<h2 class="accordion-header" id="heading-{idParser(childCategory.name)}">
						<button
							class="accordion-button collapsed"
							type="button"
							data-bs-toggle="collapse"
							data-bs-target="#collapse-{idParser(childCategory.name)}"
							aria-expanded="false"
							aria-controls="collapse-{idParser(childCategory.name)}"
						>
							<h4>
								{childCategory.name}
							</h4>
						</button>
					</h2>
					<div
						id="collapse-{idParser(childCategory.name)}"
						class="accordion-collapse collapse"
						aria-labelledby="heading-{idParser(childCategory.name)}"
						data-bs-parent="#accordionExample"
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
		object-fit: cover;
	}
	.kategorieContent {
		width: 50%;
		display: flex;
		flex-direction: column;
		align-items: center;
	}
	.accordion {
		width: 100%;
		height: 100%;
		background-color: transparent;
	}
	.accordion-item {
		background-color: transparent;
		border-color: #313539;
	}
	.accordion-header,
	.accordion-button {
		background-color: #24292d;
		text-transform: uppercase;
	}
	.accordion-button > h4 {
		margin: 0;
		color: #bfbfbf;
	}
	.accordion-button:not(.collapsed) {
		box-shadow: inset 0 calc(-1 * var(--bs-accordion-border-width)) 0 var(--bs-primary);
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
</style>

<script>
  import Image from '$lib/Image.svelte';
	import { replaceUmlauts, cleanId } from '$lib/utils.js';
	import { onMount } from 'svelte';
	import KartenProduct from './KartenProduct.svelte';
  
	onMount(async () => {
		await import('bootstrap'); // Neccessary for bootstrap to work
	});

  export let kategorie;
  const kategorie_img_name = replaceUmlauts(kategorie.name)
  let KategorieImg = import(`../../lib/assets/images/karte/${kategorie_img_name}.jpg`)
</script>

<div class="container-fluid">
  <div class="row flex-row flex-row-reverse p-0 m-0">
    <div class="col-lg-6 p-0 m-0">
      <div class="accordion accordion-flush" id="accordionExample">
	{#if kategorie.products.length > 0 }
	  <div class="accordion-body">
	    {#each kategorie.products as product}
	      <KartenProduct {product} />
	    {/each}
	  </div>
	{/if}
	{#each kategorie.childs.filter((el) => el.products.length > 0) as childCategory}
	  <div class="accordion-item">
	    <h2 class="accordion-header" id="heading-{cleanId(childCategory.name)}">
	      <button
		class="accordion-button collapsed"
		type="button"
		data-bs-toggle="collapse"
		data-bs-target="#collapse-{cleanId(childCategory.name)}"
		aria-expanded="false"
		aria-controls="collapse-{cleanId(childCategory.name)}"
		>
		<h4>
		  {childCategory.name}
		</h4>
	      </button>
	    </h2>
	    <div
	      id="collapse-{cleanId(childCategory.name)}"
	      class="accordion-collapse collapse"
	      aria-labelledby="heading-{cleanId(childCategory.name)}"
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
    <div class="col-lg-6 p-0 m-0">
      {#await KategorieImg then img}
	<Image
	  cssclass="img-fluid"
	  src={img}
	  alt={kategorie.name}
	  />
	{:catch error}
	  {error.message}
	{/await}
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

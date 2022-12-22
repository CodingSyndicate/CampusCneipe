<script>
	export let product;

	if (!product.amount) {
		product.amount = '';
	} else if (product.amount >= 0.1) {
		product.amount += 'l';
	} else if (product.amount < 0.1) {
		product.amount *= 100;
		product.amount = Math.round(product.amount);
		product.amount += 'cl';
	}
</script>

<div class="elementContainer">
	<div class="productLeft">
	  <span class="productName text-left">{product.name}
	{#each product.footnote as footnote}<sup>{footnote}</sup>{/each}
	  </span>
		<span class="productIngredients text-left">{product.ingredients}</span>
	</div>
	<span class="text-center">{product.amount}</span>
	<span class="text-right">{product.price}€</span>
</div>

<style>
	.elementContainer {
		display: grid;
		grid-template-columns: 2fr 1fr 1fr;
		width: 80%;
		margin: 0 auto;
		margin-bottom: 1.5rem;
		margin-top: 1.5rem;
		border-bottom: 2px dotted #000;
	}
	.productName {
		transition: color 0.2s;
	}
	.productName:hover {
		cursor: pointer;
		color: var(--bs-primary);
	}
	.text-right {
		text-align: right;
	}
	.productLeft {
		text-align: left;
		display: flex;
		flex-direction: column;
	}
	.productIngredients {
		font-size: 0.9rem;
		color: #8a8a8a;
	}
	@media (max-width: 666px) {
		.elementContainer {
			margin-left: 0;
			margin-right: 0;
			width: 100%;
		}
	}
</style>

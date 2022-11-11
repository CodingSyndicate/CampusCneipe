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
	<span class="productName text-left">{product.name}</span>
	<span class="productPrice text-center">{product.amount}</span>
	<span class="productPrice text-right">{product.price}€</span>
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
</style>

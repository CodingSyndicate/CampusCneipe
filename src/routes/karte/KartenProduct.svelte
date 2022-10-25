<script>
	export let product;
</script>

<div class="elementContainer">
	<span class="productName">{product.name}</span>
	<span class="productPrice">{product.price}</span>
</div>

<style>
	.elementContainer {
		display: flex;
		flex-direction: row;
		justify-content: space-between;
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
</style>

<script>
	import Template from './Template.svelte';

	// Card
	export let title;
	export let subtitle;

	// Template
	export let bigImage;
	export let contentRight;
	export let sideImageFull;
	export let sideImageHalf;
	export let sideImageThird;
	export let small;
	export let darkBackground;
</script>

<Template
	{bigImage}
	{contentRight}
	{sideImageFull}
	{sideImageHalf}
	{sideImageThird}
	{small}
	{darkBackground}
>
	<div class="col">
		<h2>{title}</h2>
		<h3>{subtitle}</h3>
		<hr />
		<slot />
	</div>
</Template>

<style>
	.col {
		padding: 8%;
		width: 100%;
		height: 100%;
	}
	h2 {
		font-size: 3.75em;
		text-transform: capitalize;
	}
	h3 {
		padding-top: 25px;
		font-size: 18px;
		padding-bottom: 0;
		margin-bottom: 0;
		text-transform: capitalize;
	}
	hr {
		width: 170px;
		height: 2px;
		background-color: var(--bs-primary);
		opacity: 1;
		padding: 0;
		margin-top: 35px;
		margin-bottom: 35px;
		border: none;
	}
	@media (max-width: 450px) {
		h2 {
			font-size: 2em;
		}
	}
</style>

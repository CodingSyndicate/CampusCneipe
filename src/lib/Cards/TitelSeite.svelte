<script>
	import { goto } from '$app/navigation';
	export let image;
	export let title;
	export let subtitle;
	export let full;
	export let middle;
	export let imagePosition = 'center';
	export let buttonLink;
	export let buttonText;
</script>

<div
	class="componentContainer"
	style="background-image: url({image}); background-position: {imagePosition}; height: {full
		? '100vh'
		: middle
		? '700px'
		: '600px'}"
>
	<div class="col">
		<h1>{title}</h1>
		<hr />
		<h2>{subtitle}</h2>
		{#if buttonText || buttonLink}
			<button type="button" class="btn btn-primary" on:click={() => goto(buttonLink)}>
				{buttonText}
			</button>
		{/if}
	</div>
</div>

<style>
	.componentContainer {
		background-repeat: no-repeat;
		background-size: cover;
		width: 100%;
		height: 100vh;
		margin: 0;
	}
	.col {
		width: 100%;
		height: 100%;
		display: flex;
		flex-direction: column;
		align-items: center;
		justify-content: center;
		text-align: center;
	}
	hr {
		height: 3px;
		border: none;
	}
	h2 {
		width: 850px;
		word-wrap: break-word;
	}
	@media (max-width: 1000px) {
		h2 {
			width: 80%;
		}
	}
</style>

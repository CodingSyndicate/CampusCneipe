<script>
	import { goto } from '$app/navigation';
	import Card from './Card.svelte';

	// DetailedCard
	export let smallImageLeft;
	export let smallImageRight;
	export let text;
	export let buttonLink;
	export let buttonText;

	// Card
	export let title;
	export let subtitle;

	// Template
	export let contentRight;
	export let bigImage;
	export let darkBackground;
</script>

<Card {title} {subtitle} {contentRight} sideImageThird={true} {bigImage} {darkBackground}>
	{#if smallImageLeft || smallImageRight}
		<div class="smallImageRow row">
			{#if smallImageLeft}
				<div class="smallImage">
					<img src={smallImageLeft} alt="smallImageLeft" />
				</div>
			{/if}
			{#if smallImageRight}
				<div class="smallImage">
					<img src={smallImageRight} alt="smallImageRight" />
				</div>
			{/if}
		</div>
	{/if}
	{#if text}
		<p>{text}</p>
	{/if}
	{#if buttonText || buttonLink}
		<button type="button" class="btn btn-outline-primary" on:click={() => goto(buttonLink)}>
			{buttonText}
		</button>
	{/if}
</Card>

<style>
	.smallImageRow {
		display: flex;
		flex-direction: row;
		justify-content: space-evenly;
		align-items: center;
		width: 100%;
		margin-bottom: 2rem;
		margin-top: 2rem;
	}
	.smallImage {
		width: 300px;
		height: 200px;
		display: flex;
		align-items: center;
		justify-content: center;
		margin: 1em;
	}
	img {
		width: 100%;
		height: 100%;
		object-fit: cover;
	}
	p {
		margin-top: 2rem;
		margin-bottom: 2rem;
	}
</style>

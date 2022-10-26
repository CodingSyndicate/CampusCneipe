<script>
        let currentDate = new Date();
	import EventPreview from './EventPreview.svelte';
	export let events;
</script>

<div class="rowContainer">
	{#each events as event}
	{#if event.date > currentDate}
		<EventPreview {event} />
	{/if}
	{/each}
</div>

<style>
	.rowContainer {
		min-height: 660px;
		width: 100%;
		background-color: #24292d;
		display: flex;
		flex-direction: row;
		align-items: center;
		justify-content: space-evenly;
		flex-wrap: wrap;
	}
	@media (max-width: 992px) {
		.rowContainer {
			flex-direction: column;
			height: auto;
		}
	}
</style>

<script>
	import { getContext } from 'svelte';
	import { TABS } from './Tabs.svelte';
	export let widthDividor;
	const tab = {};
	const { registerTab, selectTab, selectedTab } = getContext(TABS);

	registerTab(tab);
</script>

<button
	class:selected={$selectedTab === tab}
	on:click={() => selectTab(tab)}
	style="width: {100 / widthDividor}%;"
>
	<slot />
</button>

<style>
	button {
		background: none;
		border: none;
		margin: 0;
		color: #ccc;
	}

	button:hover {
		border-bottom: 2px inset var(--bs-primary);
		color: var(--bs-primary);
	}

	.selected {
		border-bottom: 2px inset var(--bs-primary);
		color: var(--bs-primary);
	}
</style>

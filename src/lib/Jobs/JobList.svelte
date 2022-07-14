<script>
	import { Row, Col } from 'svelte-chota';
	import JobsCard from './JobsCard.svelte';
	export let title;
	export let jobs = [];
</script>

<Col>
	{#if title}
		<h2>{title}</h2>
	{/if}
	<Row />
	<Row>
		{#each jobs as job}
			<JobsCard {job} />
		{:else}
			<p>Keine Jobs vorhanden</p>
		{/each}
	</Row>
</Col>

<script>
	import { Card, Button } from 'svelte-chota';
	import { goto } from '$app/navigation';

	export let title = 'Card List';
	export let elseText = 'Es wurden keine gefunden..';
	export let events = [];
</script>

<div class="cardList is-center">
	<h1>{title}</h1>
	<div class="liste">
		{#each events as event}
			<div style="max-width:400px; margin: 1rem;">
				<Card>
					<h4 slot="header">{event.name}</h4>
					{#if event.image}
						<img src={event.image} alt={event.description} />
					{/if}
					<div slot="footer">
						<div class="is-left">
							{#if event.angebot}
								<span>{event.angebot}</span>
							{/if}
						</div>
						<div class="is-right">
							{#if event.anmeldeURL && event.date >= new Date()}
								<Button primary on:click={() => goto(event.anmeldungURL)}>Anmeldung</Button>
							{/if}
						</div>
					</div>
				</Card>
			</div>
		{:else}
			<span>{elseText}</span>
		{/each}
	</div>
</div>

<style>
	.cardList {
		display: flex;
		flex-direction: column;
		padding: 1em;
	}
	.liste {
		display: flex;
		flex-direction: row;
	}
</style>

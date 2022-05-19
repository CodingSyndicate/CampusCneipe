<script>
	export let otherside = false;
	export let category;

	let innerWidth;
	function removeSeperator(text) {
		return text.split('/');
	}
</script>

<svelte:window bind:innerWidth />

<section style="background-color: {category.color}; {otherside ? 'flex-direction: row-reverse;' : ''}">
	<img src={category.image} alt={category.name} />
	<div class="cardContainer">
		<div class="header" style={otherside ? 'justify-content: flex-end;' : ''}>
			<h2 style={otherside ? 'text-align: right;' : ''}>{category.name}</h2>
		</div>
		<div class="list">
			{#each category.content as item}
				<div class="item">
					<div class="name">
						<p>
							{#if innerWidth < 768}
								{removeSeperator(item.name)[0]}
								<br />
								{removeSeperator(item.name)[1] ? removeSeperator(item.name)[1] : ''}
							{:else}
								{item.name}
							{/if}
							{#if innerWidth >= 768 && item.subtitle}
								<span>- {item.subtitle}</span>
							{/if}
						</p>
						{#if innerWidth < 768 && item.subtitle}
							<span>{item.subtitle}</span>
						{/if}
						{#if item.description}
							<span>{item.description}</span>
						{/if}
					</div>
					<div class="amount is-center">
						<p>
							{#if innerWidth < 768}
								{removeSeperator(item.amount)[0]}
								<br />
								{removeSeperator(item.amount)[1] ? removeSeperator(item.amount)[1] : ''}
							{:else}
								{item.amount}
							{/if}
						</p>
					</div>
					<div class="price is-center">
						<p>
							{#if innerWidth < 768}
								{removeSeperator(item.price)[0]}€
								<br />
								{removeSeperator(item.price)[1] ? removeSeperator(item.price)[1] + '€' : ''}
							{:else}
								{item.price}€
							{/if}
						</p>
					</div>
				</div>
			{/each}
		</div>
	</div>
</section>

<style>
	section {
		display: flex;
		flex-direction: row;
	}
	img {
		width: 33%;
		object-fit: cover;
	}
	.cardContainer {
		width: 67%;
		height: 100%;
		display: flex;
		flex-direction: column;
	}
	.header {
		display: flex;
		width: 100%;
		text-align: left;
	}
	h2 {
		text-align: left;
		margin: 0;
		padding-left: 5rem;
		padding-right: 5rem;
		padding-top: 0.5rem;
		padding-bottom: 1rem;
	}
	.list {
		width: 100%;
		display: flex;
		flex-direction: column;
		padding-left: 10%;
		padding-right: 10%;
		padding-bottom: 2rem;
	}
	.item {
		display: flex;
		flex-direction: row;
		margin-bottom: 1.5rem;
	}
	.name {
		width: 35%;
		display: flex;
		flex-direction: column;
	}
	.item > div {
		min-width: 30%;
	}
	p,
	span {
		text-align: left;
	}
	p {
		margin: 0;
		padding: 0;
		font-weight: 700;
		line-height: var(--font-size);
	}
	span {
		font-size: 1.2rem;
		color: var(--color-lightGrey);
		font-weight: 400;
		line-height: 1.2rem;
	}
	@media (max-width: 768px) {
		.item {
			min-width: 0;
		}
		p {
			word-wrap: break-word;
		}
		.list {
			padding-left: 3%;
			padding-right: 3%;
		}
		.amount > p,
		.price > p {
			text-align: center;
			text-overflow: clip;
		}
	}
</style>

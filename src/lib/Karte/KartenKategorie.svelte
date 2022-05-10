<script>
	import { Row, Col } from 'svelte-chota';

	export let otherside = false;
	export let category;
</script>

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
							{item.name}
							{#if item.subtitle}
								<span>- {item.subtitle}</span>
							{/if}
						</p>
						{#if item.description}
							<span>{item.description}</span>
						{/if}
					</div>
					<div class="amount"><p>{item.amount}</p></div>
					<div class="price"><p>{item.price}</p></div>
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
		padding-left: 1rem;
		padding-right: 1rem;
		padding-bottom: 2rem;
	}
	.item {
		display: flex;
		flex-direction: row;
		margin-bottom: 1rem;
	}
	.name {
		width: 33%;
		display: flex;
		flex-direction: column;
	}
	.item > div {
		min-width: 30rem;
		padding-left: 10rem;
		padding-right: 10rem;
	}
	p,
	span {
		text-align: left;
	}
	p {
		margin: 0;
		padding: 0;
		font-weight: 700;
	}
	span {
		font-size: 1.2rem;
		margin-top: -0.5rem;
		color: var(--color-lightGrey);
		font-weight: 400;
		line-height: 1.2rem;
	}
</style>

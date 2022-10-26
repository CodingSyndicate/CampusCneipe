<script>
	import { base } from '$app/paths';
	export let event;
</script>

<div class="eventContainer">
	<a id="imagelink" href="{base}/{event.link}">
		<img src="{base}/{event.image}" alt="event image" />
	</a>
	<a id="textlink" href="{base}/{event.link}">
		<h3>
			{event.name}
		</h3>
	</a>
</div>

<style>
	.eventContainer {
		height: 660px;
		width: 25%;
		background-color: #24292d;
		display: flex;
		flex-direction: column;
	}
	img {
		height: 532px;
		width: 100%;
		opacity: 0.7;
		transition: opacity 1s, transform 1s;
		object-fit: cover;
		border: 1px solid #24292d;
	}
	img:hover {
		opacity: 1;
	}
	#imagelink {
		cursor: pointer;
	}
	#textlink {
		height: 128px;
		text-decoration: none;
		display: flex;
		align-items: center;
		justify-content: center;
	}
	h3 {
		color: #fff;
		font-weight: 600;
		margin: 0;
		padding: 0;
		transition: color 0.2s;
		cursor: pointer;
		text-transform: uppercase;
	}
	h3:hover {
		color: var(--bg-primary-color);
	}
	@media (max-width: 992px) {
		.eventContainer {
			height: auto;
			width: auto;
		}
	}
</style>

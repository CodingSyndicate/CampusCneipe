<script>
	export let bigImage;
	export let contentRight;
	export let sideImageFull;
	export let sideImageHalf;
	export let sideImageThird;
	export let small;
	export let darkBackground;
</script>

<div
	class:darkBackground
	class="rowContainer"
	style="min-height: {small ? '625px' : '902px'}; flex-direction: {contentRight
		? 'row'
		: 'row-reverse'}"
>
	<div
		class="bigImage"
		style="width: {sideImageHalf
			? '50%'
			: sideImageThird
			? '33.3333333%'
			: sideImageFull
			? '0%'
			: '0%'};
				min-height: {small ? '625px' : '902px'};"
	>
		<img
			src={bigImage}
			alt="bigImage"
			style="min-height: {small ? '625px' : '902px'}; max-height: {small ? '625px' : '902px'}"
		/>
	</div>
	<div
		class="content"
		style="width: {sideImageHalf
			? '50%'
			: sideImageThird
			? '66.666666667%'
			: sideImageFull
			? '100%'
			: '0%'};
			min-height: {small ? '625px' : '902px'};"
	>
		<slot />
	</div>
</div>

<style>
	.rowContainer {
		display: flex;
		flex-direction: row;
		justify-content: space-between;
		align-items: center;
		width: 100%;
		overflow: hidden;
	}
	.darkBackground {
		background-color: #24292d;
	}
	.content {
		height: 100%;
		min-height: 100%;
	}
	.bigImage {
		height: 100%;
		min-height: 100%;
		max-height: 100%;
	}
	img {
		width: 100%;
		height: 100%;
		min-height: 100%;
		max-height: 100%;
		object-fit: cover;
	}
	@media (max-width: 992px) {
		.rowContainer {
			flex-direction: column-reverse !important;
			min-height: 100%;
		}
		.content {
			width: 100%;
			min-width: 100%;
		}
		.bigImage {
			width: 100%;
			min-width: 100%;
		}
	}
</style>

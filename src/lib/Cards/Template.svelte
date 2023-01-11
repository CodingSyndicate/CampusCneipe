<script>
  import { base } from '$app/paths';
import Image from '$lib/Image.svelte';
  export let bigImage;
	export let contentRight;
  export let sideImageHalf;
  export let sideImageThird;
	export let small;
  export let darkBackground;
  export let noPreprocess;
</script>

<div class="container-fluid {darkBackground ? 'text-bg-dark' : ''}">
  <div class="row flex-row align-items-center {!contentRight ? '' : 'flex-row-reverse'}">
    <div class="{sideImageThird ? 'col-lg-8' : 'col-lg-6'} align-self-start flex-grow-1 p-0 m-0">
      <slot />
    </div>
    <div class="{sideImageThird ? 'col-lg-4' : 'col-lg-6'} flex-shrink-0 p-0 m-0">
      {#if noPreprocess}
	<img src={bigImage} class="img-fluid" />
	{:else}
	  <Image
	    src={bigImage}
	    alt="bigImage"
	    cssclass="img-fluid"
	    />
      {/if}
    </div>
  </div>
</div>
 
<!-- 	style="min-height: {small ? '625px' : '902px'}; flex-direction: {contentRight -->
<!-- 		? 'row' -->
<!-- 		: 'row-reverse'}" -->
<!-- > -->
<!-- 	<div -->
<!-- 		class="bigImage" -->
<!-- 		style="width: {sideImageHalf -->
<!-- 			? '50%' -->
<!-- 			: sideImageThird -->
<!-- 			? '33.3333333%' -->
<!-- 			: sideImageFull -->
<!-- 			? '0%' -->
<!-- 			: '0%'}; -->
<!-- 				min-height: {small ? '625px' : '902px'};" -->
<!-- 	> -->
<!-- 		<Image -->
<!-- 			src={bigImage} -->
<!-- 			alt="bigImage" -->
<!-- 			style="min-height: {small ? '625px' : '902px'}; max-height: {small ? '625px' : '902px'}" -->
<!-- 		/> -->
<!-- 	</div> -->
<!-- 	<div -->
<!-- 		class="content" -->
<!-- 		style="width: {sideImageHalf -->
<!-- 			? '50%' -->
<!-- 			: sideImageThird -->
<!-- 			? '66.666666667%' -->
<!-- 			: sideImageFull -->
<!-- 			? '100%' -->
<!-- 			: '0%'}; -->
<!-- 			min-height: {small ? '625px' : '902px'};" -->
<!-- 	> -->
<!-- 		<slot /> -->
<!-- 	</div> -->
<!-- </div> -->

<!-- <style> -->
<!-- 	.rowContainer { -->
<!-- 		display: flex; -->
<!-- 		flex-direction: row; -->
<!-- 		justify-content: space-between; -->
<!-- 		align-items: center; -->
<!-- 		width: 100%; -->
<!-- 		overflow: hidden; -->
<!-- 	} -->
<!-- 	.darkBackground { -->
<!-- 		background-color: #24292d; -->
<!-- 	} -->
<!-- 	.content { -->
<!-- 		height: 100%; -->
<!-- 		min-height: 100%; -->
<!-- 	} -->
<!-- 	.bigImage { -->
<!-- 		height: 100%; -->
<!-- 		min-height: 100%; -->
<!-- 		max-height: 100%; -->
<!-- 	} -->
<!-- 	img { -->
<!-- 		width: 100%; -->
<!-- 		height: 100%; -->
<!-- 		min-height: 100%; -->
<!-- 		max-height: 100%; -->
<!-- 		object-fit: cover; -->
<!-- 	} -->
<!-- 	@media (max-width: 992px) { -->
<!-- 		.rowContainer { -->
<!-- 			flex-direction: column-reverse !important; -->
<!-- 			min-height: 100%; -->
<!-- 		} -->
<!-- 		.content { -->
<!-- 			width: 100%; -->
<!-- 			min-width: 100%; -->
<!-- 		} -->
<!-- 		.bigImage { -->
<!-- 			width: 100%; -->
<!-- 			min-width: 100%; -->
<!-- 		} -->
<!-- 	} -->
<!-- </style> -->

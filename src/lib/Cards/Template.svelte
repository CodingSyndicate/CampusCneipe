<script>
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
    <div class="{sideImageThird ? 'col-lg-8' : 'col-lg-6'} flex-grow-1 p-0 m-0">
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
 

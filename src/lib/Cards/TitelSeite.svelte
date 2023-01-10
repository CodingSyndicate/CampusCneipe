<script>
  import { goto } from '$app/navigation';
  import Image from '$lib/Image.svelte';
	import { base } from '$app/paths';
	export let image;
	export let title;
	export let subtitle;
	export let full;
	export let middle;
	export let imagePosition = 'center';
	export let buttonLink;
	export let buttonText;
</script>


<div class="container-fluid p-0 m-0 g-0">
  <div class="card text-center border-0 text-bg-dark" style="min-height: 300px;">
    <div class="row align-items-center p-0 m-0 g-0">
      <Image src={image} cssclass="{full ? 'card-img' : 'card-img-top'}" />
      <div class="{full ? 'card-img-overlay' : 'card-body'}">
	<div class="col align-self-center p-0 m-0 g-0">
 	  <h1 class="card-title">{title}</h1>
	  <hr />
	  <h4 class="card-title">{@html subtitle}</h4>
	  {#if buttonText || buttonLink}
	    <p class="card-text">
	      <button type="button" class="btn btn-primary" on:click={() => goto(buttonLink)}>
		{buttonText}
	      </button>
	    </p>
	  {/if}
	</div>
      </div>
    </div>
  </div>
</div>

<!--  <div -->
<!-- 	class="componentContainer" -->
<!-- 	style="background-image: url({base + image}); background-position: {imagePosition}; height: {full -->
<!-- 		? '100vh' -->
<!-- 		: middle -->
<!-- 		? '700px' -->
<!-- 		: '600px'}" -->
<!-- > -->
<!-- 	<div class="col"> -->
<!-- 		<h1>{title}</h1> -->
<!-- 		<hr /> -->
<!-- 		<h2>{@html subtitle}</h2> -->
<!-- 		{#if buttonText || buttonLink} -->
<!-- 			<button type="button" class="btn btn-primary" on:click={() => goto(buttonLink)}> -->
<!-- 				{buttonText} -->
<!-- 			</button> -->
<!-- 		{/if} -->
<!-- 	</div> -->
<!-- </div> -->

<style>
	.col {
		width: 100%;
		height: 100%;
		display: flex;
		flex-direction: column;
		align-items: center;
		justify-content: center;
		text-align: center;
	}
	hr {
		height: 3px;
		border: none;
		margin: 5px;
	}
	h1 {
	  text-transform: uppercase;
	  font-size: 2em;
	}
	h4 {
	  word-wrap: break-word;
	}
	@media (max-width: 1000px) {
		h2 {
			width: 80%;
		}
	}
</style>

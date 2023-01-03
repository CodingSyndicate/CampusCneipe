<script>
  export let src;
  export let alt;
  export let style;
  export let cssclass;
</script>

<picture>

	{#each Object.entries(src.sources) as [format, images]}
	  <source
	    srcset="{images.map(({src, w}) => `${src} ${w}w`).join(', ')}"
	    type={'image/' + format} /> 
	{/each}
	<img src={src.fallback.src} alt={alt} style={style} class={cssclass} loading="lazy" />
</picture>

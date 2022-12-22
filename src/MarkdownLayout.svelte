<script>
  export let title;
  export let description = "";
</script>  

<svelte:head>
	<title>{title} | CampusCneipe</title>
	<meta name="description" content={description} />
	<meta property="og:title" content={title} />
	<meta property="og:image" content="https://www.c2.tum.de/images/Hintergrundbild.jpg" />
</svelte:head>


<div class="container">
  <div class="row ps-2">
    <div class="col-lg-8">
      <slot>
      </slot>
    </div>
  </div>
</div>

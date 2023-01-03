<script>
	import TitelSeite from '$lib/Cards/TitelSeite.svelte';
  import Karte from './Karte.svelte';
  import KartenImg from "$lib/assets/images/6-2.png";
</script>

<svelte:head>
	<title>Karte | CampusCneipe</title>
	<meta name="description" content="Karte aller Getränke und Speisen der Campus Cneipe" />
	<meta property="og:title" content="Getränkekarte der Campus Cneipe" />
	<meta property="og:image" content="https://www.c2.tum.de/images/Hintergrundbild.jpg" />
	<meta property="og:url" content="https://www.c2.tum.de/karte" />
	<meta property="og:site_name" content="Getränkekarte der Campus Cneipe" />
	<meta property="og:description" content="Karte aller Getränke und Speisen der Campus Cneipe" />
</svelte:head>

<TitelSeite
	title="Getränke- und Speisekarte"
	subtitle='<div class="buttons"><a href="/menu.pdf">
		    <button type="button" class="btn btn-primary">
		      PDF
		    </button>
		  </a></div>'
	full={false}
	middle={false}
	image={KartenImg}
	imagePosition="bottom"
/>

<Karte />

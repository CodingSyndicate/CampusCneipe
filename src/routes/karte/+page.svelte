<script>
	import TitelSeite from '$lib/Cards/TitelSeite.svelte';
	import Karte from './Karte.svelte';
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
	title="GETRÄNKE- UND SPEISEKARTE"
	subtitle="BIER, COCKTAILS, SHOTS, LONGDRINKS, SOFTDRINKS, SNACKS, KAFFEE UND NOCH MEHR BIER..."
	full={false}
	middle={false}
	image="/images/6-2.png"
	imagePosition="bottom"
/>
<Karte />

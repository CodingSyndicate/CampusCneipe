<script>
	import { Container, Button } from 'svelte-chota';
	import Gallery from 'svelte-image-gallery';

	const images = [
		{ src: './images/mieten/Brotzeit.jpg' },
		{ src: './images/mieten/Brotzeitplatten.jpg' },
		{ src: './images/mieten/Catering.jpg' },
		{ src: './images/mieten/Cneipe.jpg' },
		{ src: './images/mieten/Essen1.jpg' },
		{ src: './images/mieten/Essen2.jpg' },
		{ src: './images/mieten/Essen3.jpg' },
		{ src: './images/mieten/Essen4.jpg' },
		{ src: './images/mieten/Essen5.jpg' },
		{ src: './images/mieten/Essen6.jpg' },
		{ src: './images/mieten/Essen7.jpg' },
		{ src: './images/mieten/Käse1.jpg' },
		{ src: './images/mieten/Käse2.jpg' },
		{ src: './images/mieten/Kindergeburstag.jpg' },
		{ src: './images/mieten/Kommunion1.jpg' },
		{ src: './images/mieten/Kommunion2.jpg' },
		{ src: './images/mieten/Kommunion3.jpg' },
		{ src: './images/mieten/Kommunion4.jpg' },
		{ src: './images/mieten/Kommunion5.jpg' },
		{ src: './images/mieten/Kommunion6.jpg' },
		{ src: './images/mieten/Kommunion7.jpg' },
		{ src: './images/mieten/Kommunion8.jpg' },
		{ src: './images/mieten/Kommunion9.jpg' },
		{ src: './images/mieten/mieten1.jpg' },
		{ src: './images/mieten/mieten2.jpg' },
		{ src: './images/mieten/mieten3.jpg' },
		{ src: './images/mieten/mieten4.jpg' },
		{ src: './images/mieten/Tische1.jpg' },
		{ src: './images/mieten/Tische2.jpg' },
		{ src: './images/mieten/Tische3.jpg' },
		{ src: './images/mieten/Tische4.jpg' },
		{ src: './images/mieten/Tische5.jpg' },
		{ src: './images/mieten/Wurst1.jpg' },
		{ src: './images/mieten/Wurst2.jpg' }
	];
	let loadGallery;
</script>

<svelte:head>
	<title>Mieten | CampusCneipe</title>
	<meta name="description" content="Die C2 als Veranstaltungsort mieten" />
	<meta property="og:title" content="Campus Cneipe mieten" />
	<meta property="og:image" content="https://www.c2.tum.de/images/Hintergrundbild.jpg" />
	<meta property="og:url" content="https://www.c2.tum.de/mieten" />
	<meta property="og:site_name" content="Campus Cneipe mieten" />
	<meta property="og:description" content="Die C2 als Veranstaltungsort mieten" />
</svelte:head>

<div class="is-full-screen">
	<Container>
		<h1>Die C2 als Veranstaltungsort mieten</h1>
		<h5 style="margin-top: -2.5rem;">Ihr sucht eine besondere Location, in der eure Privatfeier ein voller Erfolg wird? <br /> Dann seid ihr bei uns genau richtig!</h5>
		<p>
			Das Team der CampusCneipe C2 betreut Euch zuverlässig und kompetent, um Euch eine sorglose und unbeschwerte Feier zu ermöglichen. Ein zentraler Ansprechpartner betreut Euch und Euer Event von
			der ersten Kontaktaufnahme über die Planung und Durchführung bis hin zur Abrechnung des Events. Seit der Eröffnung im Jahr 2005 fanden bereits hunderte verschiedene Events bei uns statt - ob
			Studentenparty, Doktorfeier, Geburtstagsfeiern, Kommunionen oder Weihnachtsfeiern.
		</p>
		<img src="./images/mieten/mieten4.jpg" alt="" />
		<section>
			<h5>Unsere Leistungen im Überblick</h5>
			<ul>
				<li>
					Unsere Cneipe bietet Sitzplätze für rund 80-90 Personen, bei größeren Parties Stehplätze für bis zu 200 Personen. Im Sommer lässt sich zudem der Mensa-Innenhof als Außenbereich nutzen (keine
					Bewirtung am Tisch). Die Cneipe verfügt über eine moderne Bar mit Fasskühlung, Gästetoiletten, einen Tischkicker und einer (Brett-)Spielecke.
				</li>
				<li>
					Wir stellen Euch unsere Räumlichkeiten zur Verfügung. Ihr bezahlt dabei keine hohe Raummiete, sondern nur eine kleine Pauschale von 70€ sowie die Personalausgaben am Tag eurer Feier. Gerne
					erstellen wir einen unverbindlichen Kostenvoranschlag für Euer Event.
				</li>
				<li>Unser Servicepersonal versorgt Euch mit Bieren, Softdrinks, erlesenen Weinen und fruchtigen Cocktails. Gerne führen wir auch einen Sektempfang bei uns durch.</li>
				<li>Gerne kümmern wir uns auch um die Verpflegung eurer Gäste (siehe CampusCneipe kocht). Ihr könnt aber auch kostenfrei eigene Snacks mitbringen oder externes Catering organisieren.</li>
			</ul>
		</section>
		<img src="./images/mieten/mieten3.jpg" alt="" />
		<section>
			<h5>CampusCneipe kocht</h5>
			<h6>Unser Essensangebot bei Privatfeiern umfasst:</h6>
			<ul>
				<li>Grillen am Holzkohlegrill (Nackensteak, Würstchen, Grillkäse, Gemüse etc.)</li>
				<li>Saugrillen</li>
				<li>Bayerische Brotzeitplatten</li>
				<li>Fingerfood (Canapée)</li>
				<li>Leberkäse</li>
				<li>Weißwurstfrühstück</li>
				<li>Nudel- und Reisgerichte</li>
				<li>Uvm.</li>
			</ul>
			<p>Gerne kommen wir mit unseren Speisen auch zu Euch an den Lehrstuhl/nach Hause und verpflegen eure Gäste vor Ort.</p>
		</section>
		<img src="./images/mieten/mieten1.jpg" alt="" />

		<section>
			<h5>Auswahl unserer bisherigen Events:</h5>
			<ul>
				<li>Doktorfeiern</li>
				<li>Firmen- und Lehrstuhl-Weihnachtsfeiern</li>
				<li>Geburtstage - Jubilare von 2 bis 80 Jahren</li>
				<li>18. Geburtstage</li>
				<li>Kommunionen</li>
				<li>Abschlussfeiern</li>
				<li>Teamevents</li>
				<li>Karaoke-Partys</li>
				<li>Pubcrawls</li>
			</ul>
		</section>
		<img src="./images/mieten/mieten2.jpg" alt="" />
		<section>
			<h5>Interesse geweckt?</h5>
			<p>Schreibe uns gerne eine Email und wir planen gemeinsam Dein Event!</p>
			<p>Kontakt: <a href="mailto:events@campus-cneipe.de">events@campus-cneipe.de</a></p>
		</section>
		<div class="galleryContainer is-center">
			{#if loadGallery}
				<Gallery gap="10" maxColumnWidth="300">
					{#each images as image}
						<img src={image.src} alt="" />
					{/each}
				</Gallery>
			{:else}
				<Button primary on:click={() => (loadGallery = true)}>Impressionen vergangener Veranstaltungen</Button>
			{/if}
		</div>
	</Container>
</div>

<style>
	h5 {
		font-weight: 700;
	}
	h6 {
		margin-top: -1.5rem;
	}
	:global(img) {
		opacity: 0.9;
		transition: all 0.2s;
	}
	:global(img):hover {
		opacity: 1;
		transform: scale(1.04);
	}
	.galleryContainer {
		margin-top: 4rem;
		margin-bottom: 4rem;
	}
</style>

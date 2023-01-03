<script>
	import Card from '$lib/Cards/Card.svelte';
  import TitelSeite from '$lib/Cards/TitelSeite.svelte';
  import TitelImg from '$lib/assets/images/mieten/IMG_5866.jpg?height=600px&position=cover';
  import CneipenImg from '$lib/assets/images/mieten/Cneipe.jpg';
  import Mieten3 from '$lib/assets/images/mieten/mieten3.jpg';
  import Mieten1 from '$lib/assets/images/mieten/mieten1.jpg';
  import Mieten2 from '$lib/assets/images/mieten/mieten2.jpg';
  import ImgUnten from '$lib/assets/images/mieten/mieten4-dark.png';
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
<TitelSeite
	title="Die C2 als Veranstaltungsort mieten"
	subtitle="Ihr sucht eine besondere Location, in der Eure Privatfeier ein voller Erfolg wird? Dann seid
	Ihr bei uns genau richtig!"
	full={false}
	middle={false}
	image={TitelImg}
	imagePosition="center"
  />
<Card
	contentRight={false}
	sideImageHalf={true}
	small={true}
	title="Ihre Veranstaltung"
	subtitle="Alles ist möglich"
  bigImage={CneipenImg}
  >
	<p>
		Das Team der CampusCneipe C2 betreut Euch zuverlässig und kompetent, um Euch eine sorglose und
		unbeschwerte Feier zu ermöglichen. Ein zentraler Ansprechpartner betreut Euch und Euer Event von
		der ersten Kontaktaufnahme über die Planung und Durchführung bis hin zur Abrechnung des Events.
	</p>
	<p>
		Seit der Eröffnung im Jahr 2005 fanden bereits hunderte verschiedene Events bei uns statt - ob
		Studentenparty, Doktorfeier, Geburtstagsfeiern, Kommunionen oder Weihnachtsfeiern.
	</p>
</Card>
<Card
	contentRight={true}
	sideImageHalf={true}
	small={true}
	title="Unsere Leistungen"
	subtitle="Voller Einsatz für Sie"
	bigImage={Mieten3}
>
	<ul>
		<li>
			Unsere Cneipe bietet Sitzplätze für rund 80-90 Personen, bei größeren Parties Stehplätze für
			bis zu 200 Personen. Im Sommer lässt sich zudem der Mensa-Innenhof als Außenbereich nutzen
			(keine Bewirtung am Tisch). Die Cneipe verfügt über eine moderne Bar mit Fasskühlung,
			Gästetoiletten, einen Tischkicker und einer (Brett-)Spielecke.
		</li>
		<li>
			Wir stellen Euch unsere Räumlichkeiten zur Verfügung. Ihr bezahlt dabei keine hohe Raummiete,
			sondern nur eine kleine Pauschale von 70€ sowie die Personalausgaben am Tag eurer Feier. Gerne
			erstellen wir einen unverbindlichen Kostenvoranschlag für Euer Event.
		</li>
		<li>
			Unser Servicepersonal versorgt Euch mit Bieren, Softdrinks, erlesenen Weinen und fruchtigen
			Cocktails. Gerne führen wir auch einen Sektempfang bei uns durch.
		</li>
		<li>
			Gerne kümmern wir uns auch um die Verpflegung eurer Gäste (siehe CampusCneipe kocht). Ihr
			könnt aber auch kostenfrei eigene Snacks mitbringen oder externes Catering organisieren.
		</li>
	</ul>
</Card>
<Card
	contentRight={false}
	sideImageHalf={true}
	small={true}
	title="Campuscneipe kocht"
	subtitle="Unser Essensangebot bei Privatfeiern umfasst:"
	bigImage={Mieten1}
>
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
	<p>
		Gerne kommen wir mit unseren Speisen auch zu Euch an den Lehrstuhl/nach Hause und verpflegen
		eure Gäste vor Ort.
	</p>
</Card>
<Card
	contentRight={true}
	sideImageHalf={true}
	small={true}
	title="Unsere Erfahrung"
	subtitle="Auswahl bisheriger Events:"
	bigImage={Mieten2}
>
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
</Card>
<TitelSeite
	title="Interesse geweckt?"
	subtitle="Kontaktiere uns und wir planen gemeinsam dein Event!"
	full={false}
	middle={false}
	image={ImgUnten}
	imagePosition="center"
	buttonText="Kontakt aufnehmen!"
	buttonLink="/kontakt"
/>

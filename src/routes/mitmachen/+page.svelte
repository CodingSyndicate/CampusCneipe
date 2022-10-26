<script>
	import TitelSeite from '$lib/Cards/TitelSeite.svelte';
	import { base } from '$app/paths';
</script>

<svelte:head>
	<title>Mitmachen | CampusCneipe</title>
	<meta name="description" content="Du willst mitmachen? Dann bewerb dich!" />
	<meta property="og:title" content="Du willst mitmachen? Dann bewerb dich!" />
	<meta property="og:image" content="https://www.c2.tum.de/images/Hintergrundbild.jpg" />
	<meta property="og:url" content="https://www.c2.tum.de/mitmachen" />
	<meta property="og:site_name" content="Du willst mitmachen? Dann bewerb dich!" />
	<meta property="og:description" content="Du willst mitmachen? Dann bewerb dich!" />
</svelte:head>

<TitelSeite
	title="MITMACHEN"
	subtitle="Im Service, hinterm Tresen oder gar im Lager!"
	full={false}
	middle={false}
	image="/images/job.png"
	imagePosition="top"
/>

<div class="is-full-screen">
	<div class="content">
		<h3>12-14€ STUDENLOHN ALS...</h3>
		<div class="dauerJobs">
			<section>
				<h4>MITARBEITER SERVICE</h4>
				<pre>Du hast gerne Kontakt mit Menschen,
stellst es dir cool vor,
hinter einer Bar zu arbeiten
und mischt gerne Cocktails??</pre>
			</section>
			<section>
				<h4>MITARBEITER KÜCHE</h4>
				<pre>Du wolltest schon immer mal deinen Kochkünsten
in einer Gastroküche freien Lauf lassen
oder dich wie bei fast keinem anderen Betrieb
in die Planung der Gerichte und Rezepte einbringen?</pre>
			</section>
		</div>
		<pre class="bottomPre"><h4>DANN BEWIRB DICH JETZT
UND WERDE TEIL UNSERES TEAMS!</h4>
Mit dem Schichtplaner Tool kannst du dir deine Arbeitszeiten individuell einteilen und dir so mit 
<b>12-14€ Stundenlohn</b> etwas dazuverdienen.

Mail an info@campus-cneipe.de
oder smash den Button!</pre>
		<a href="{base}/kontakt"
			><button type="button" class="btn btn-outline-primary">Teil der C2 werden!</button></a
		>
	</div>
</div>

<style>
	.content {
		display: flex;
		flex-direction: column;
		align-items: center;
		justify-content: center;
		width: 100%;
		height: 100%;
	}
	.dauerJobs {
		display: flex;
		flex-direction: row;
		align-items: center;
		justify-content: center;
		width: 100%;
	}
	section {
		box-shadow: 0 1px 3px rgba(0, 0, 0, 0.12), 0 1px 2px rgba(0, 0, 0, 0.24);
		transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1);
		border-radius: 2px;
		width: 40%;
		padding: 1rem;
		margin-left: 3rem;
		margin-right: 3rem;
		position: relative;
		display: flex;
		flex-direction: column;
		align-items: center;
		background-color: #24292d;
	}
	h3 {
		margin: 2rem;
		font-weight: 900;
	}
	h4 {
		margin-bottom: 0;
		text-align: center;
	}
	pre {
		white-space: pre-wrap;
		text-align: center;
	}
	.bottomPre {
		margin-top: 2rem;
		background-color: transparent;
	}
	a {
		margin-bottom: 2rem;
	}
	@media (max-width: 768px) {
		.dauerJobs {
			flex-direction: column;
		}
		section {
			width: 90%;
			margin-top: 1rem;
		}
	}
</style>

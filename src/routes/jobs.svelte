<script>
	import { jobs } from '$lib/data/jobs';

	import JobList from '$lib/Jobs/JobList.svelte';
	import { Container, Button } from 'svelte-chota';
</script>

<svelte:head>
	<title>Jobs | CampusCneipe</title>
	<meta name="description" content="Jobs an der Campus Cneipe" />
</svelte:head>

<div class="is-full-screen">
	<Container>
		<div class="content">
			<img src="./images/job.png" alt="" />
			<h3>12-14€ Studenlohn als...</h3>
			<div class="dauerJobs">
				<section>
					<h4>Mitarbeiter Service</h4>
					<pre>Du hast gerne Kontakt mit Menschen,
stellst es dir cool vor,
hinter einer Bar zu arbeiten
und mischt gerne Cocktails??</pre>
				</section>
				<section>
					<h4>Mitarbeiter Küche</h4>
					<pre>Du wolltest schon immer mal deinen Kochkünsten
in einer Gastroküche freien Lauf lassen
oder dich wie bei fast keinem anderen Betrieb
in die Planung der Gerichte und Rezepte einbringen?</pre>
				</section>
			</div>
			<pre class="bottomPre"><h4>Dann bewirb dich jetzt
und werde Teil unseres Teams!</h4>
Mit dem Schichtplaner Tool kannst du dir deine Arbeitszeiten individuell einteilen und dir so mit 
<b>12-14€ Stundenlohn</b> etwas dazuverdienen.

Mail an info@campus-cneipe.de
oder smash den Button!</pre>
			<a href="mailto:info@campus-cneipe.de"><Button primary>Teil der C2 werden!</Button></a>
			{#if jobs.length > 0}
				<hr />
				<JobList title="Spezielle Jobs" {jobs} />
			{/if}
		</div>
	</Container>
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
	img {
		width: 100%;
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
		background-color: var(--bg-secondary-color);
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
		margin-top: 0;
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

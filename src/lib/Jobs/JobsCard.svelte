<script>
	import { Button, Card } from 'svelte-chota';
	import { goto } from '$app/navigation';

	export let job = {
		title: 'Quizmaster',
		image: '/images/job.png',
		description: 'Du hast Lust dir Fragen auszudenken, endlich mit deinem unnötigen Wissen zu strahlen und willst das PubQuiz der Campus Cneipe unterstützen?',
		contact: 'events@campus-cneipe.de'
	};
</script>

<div style="max-width:400px; margin: 1rem;">
	<Card>
		<h4 slot="header">{job.title}</h4>
		<img src={job.image} alt="" />
		<pre>{job.description}</pre>
		<div slot="footer" class="is-right">
			<a href={`mailto:${job.contact}`}>
				<Button primary>Contact</Button>
			</a>
		</div>
	</Card>
</div>

<style>
	pre {
		white-space: pre-wrap;
		text-align: center;
	}
</style>

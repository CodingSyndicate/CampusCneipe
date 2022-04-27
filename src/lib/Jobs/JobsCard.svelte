<script>
	import { Button, Card } from 'svelte-chota';
	import { goto } from '$app/navigation';

	let ID = 0;
	let title = 'Quizmaster';
	let image = '/images/job.png';
	let description = 'Du hast Lust dir Fragen auszudenken, endlich mit deinem unnötigen Wissen zu strahlen und willst das PubQuiz der Campus Cneipe unterstützen?';
	let contact = 'events@campus-cneipe.de';
</script>

<div style="max-width:300px; margin: 1rem;">
	<Card>
		<h4 slot="header">{title}</h4>
		<img src={image} alt={title} />
		{description}
		<div slot="footer" class="is-right">
			<Button primary on:click={() => goto(`/jobs/${ID}`)}>Details</Button>
		</div>
	</Card>
</div>

<script>
  import opening_times from '$data/opening_times.json';
  import { goto } from '$app/navigation';
  import Card from '$lib/Cards/Card.svelte';
  let bigImage = '/images/7.jpg';

  let options = {
//    weekday: 'long',
    year: '2-digit',
    month: 'numeric',
    day: 'numeric',
//    hour: 'numeric',
//    minute: 'numeric',
    timeZone: 'Europe/Berlin'
  };
  
  for (let vacation in opening_times.vacations) {
    opening_times.vacations[vacation].begin_date = Date.parse(opening_times.vacations[vacation].from)
    opening_times.vacations[vacation].begin_text = new Intl.DateTimeFormat('de-DE', options).format(opening_times.vacations[vacation].begin_date)
    opening_times.vacations[vacation].end_date = Date.parse(opening_times.vacations[vacation].to)
    opening_times.vacations[vacation].end_text = new Intl.DateTimeFormat('de-DE', options).format(opening_times.vacations[vacation].end_date)

  }
  let day_milliseconds = 1000 * 60 * 60 * 24;
  let cutoff = new Date().getTime() + 20 * day_milliseconds;

  opening_times.vacations.sort((a, b) => {
    if (a.begin_date < b.begin_date) return -1;
    else return 1;
  });
  let display_vacation = opening_times.vacations.filter(v => v.begin_date - cutoff < 0)[0];
</script>

<Card
	title="Öffnungszeiten"
	subtitle="Während der Vorlesungzeit"
	{bigImage}
	contentRight={true}
	sideImageHalf={true}
	small={true}
	darkBackground={true}
  >
  {#if display_vacation}
      <div class="alert alert-danger">
	Von {display_vacation.begin_text} bis {display_vacation.end_text} wegen {display_vacation.name} geschlossen!
      </div>
    {/if}

  <table class="table mt-3 table-borderless text-light">
      <tbody>
	{#each opening_times.days as day}
	  <tr>
	    <th>{day.day}</th>
	    <th>{day.open}</th>
	    <th>-</th>
	    <th>{day.close}</th>
	  </tr>
	{/each}
      </tbody>
  </table>

		<p>
		Außerhalb der Vorlesungszeit haben wir für den regulären Betrieb geschlossen. Die Campus Cneipe
		kann aber weiterhin für Veranstaltungen jeglicher Art gebucht werden.
	</p>
	<div class="buttons">
		<button type="button" class="btn btn-primary" on:click={() => goto('/kontakt')}>
			Tisch reservieren
		</button>
		&nbsp;
		<button type="button" class="btn btn-outline-primary" on:click={() => goto('/mieten')}>
			C2 mieten
		</button>
	</div>
</Card>

<style>
	button {
		margin-top: 0.5rem;
	}
	p {
		margin-top: 2rem;
		margin-bottom: 2rem;
	}
</style>

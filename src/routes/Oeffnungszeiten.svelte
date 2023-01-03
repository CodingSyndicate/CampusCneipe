<script>
  import opening_times from '$data/opening_times.json';
  import notices from '$data/notices.json';
  import { goto } from '$app/navigation';
  import Card from '$lib/Cards/Card.svelte';
  import bigImage from '$lib/assets/images/7.jpg';

  function convert_date(date_string) {
    let options = {
      year: '2-digit',
      month: 'numeric',
      day: 'numeric',
      timeZone: 'Europe/Berlin'
      };
    return new Intl.DateTimeFormat('de-DE', options).format(date_string);
  }
  
  for (let notice in notices) {
    notices[notice].date_display_from = Date.parse(notices[notice].display_from)
    notices[notice].date_display_until = Date.parse(notices[notice].display_until)
  }
  let now = new Date().getTime();
  notices.sort((a, b) => {
    if (a.date_display_from < b.date_display_until) return -1;
    else return 1;
  });
  let display_notices = notices.filter(n =>
    n.date_display_from < now && n.date_display_until > now);
</script>

<Card
	title="Öffnungszeiten"
	subtitle=""
	bigImage={bigImage}
	contentRight={true}
	sideImageHalf={true}
	small={true}
	darkBackground={true}
  >
  {#each display_notices as notice}
    <div class="alert alert-danger">
      <h4 class="alert-heading">&#9888; {notice.title}</h4>
      <hr />
      <p class="text-black">{notice.text}</p>
      </div>
    {/each}

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
		  Die Campus Cneipe kann jederzeit für Veranstaltungen aller Art gebucht werden.
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

<script>
  import opening_times from '$data/opening_times.json';
  import { goto } from '$app/navigation';
  import Card from '$lib/Cards/Card.svelte';
  import bigImage from '$lib/assets/images/7.jpg';
  export let notices;
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
  {#await notices then display_notices}
  {#each display_notices as notice}
    <div class="alert alert-danger">
      <h4 class="alert-heading">&#9888; {notice.title}</h4>
      <hr />
      <p class="text-black">{notice.text}</p>
      </div>
    {/each}
  {/await}

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

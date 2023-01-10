<script>
  import { onMount } from 'svelte';
  import Card from '$lib/Cards/Card.svelte';
  export let event;
  export let textRight = false;
  if (!event.png_image) {
    event.png_image = 'default';
  }
  let options = {
    weekday: 'long',
    year: 'numeric',
    month: 'numeric',
    day: 'numeric',
    hour: 'numeric',
    minute: 'numeric',
    timeZone: 'Europe/Berlin'
  };
  event.begin_string = new Intl.DateTimeFormat('de-DE', options).format(event.begin);
  let EventImage = import(`$lib/assets/images/events/${event.png_image}.png`)    
</script>

{#await EventImage then img}
  {#key img}
<Card
  contentRight={textRight}
  sideImageHalf={true}
  title={event.title}
  subtitle={event.begin_string}
  bigImage={img}
  small={true}
  noPreprocess={false}
>
	{@html event.description}
</Card>
{/key}
{:catch error}
  {error.message}
{/await}

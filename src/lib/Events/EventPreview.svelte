<script>
  import { onMount } from 'svelte';
  import Card from '$lib/Cards/Card.svelte';
  import { base } from '$app/paths';
  export let event;
  export let textRight = false;
  //needs to be this way
  let EventImage
  if (event.image.endsWith('.png')) {
    let img_filename = event.image.substr(0, event.image.length - 4)
    EventImage = import(`$lib/assets/images/events/${img_filename}.png`)
  } else if (event.image.endsWith('.jpg')) {
    let img_filename = event.image.substr(0, event.image.length - 4)
    EventImage = import(`$lib/assets/images/events/${img_filename}.jpg`)
  } else {
    let img_filename = 'default.png'
    EventImage = import('$lib/assets/images/events/default.png')
  }
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

<script>
  import { onMount } from 'svelte';
	import Card from '$lib/Cards/Card.svelte';
	import { base } from '$app/paths';
  export let event;
    export let textRight = false;
	let link;
	if (!event.link) {
		link = './';
	} else if (event.link.startsWith('http')) {
		link = event.link;
	} else {
		link = base + event.link;
	}
  if (!event.image) {
    event.image = 'default.png';
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

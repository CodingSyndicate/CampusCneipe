<script>
  import Card from '$lib/Cards/Card.svelte';
  import { base } from '$app/paths';
  export let event;
  let link;
  if (!event.link) {
    link = './';
  } else if (event.link.startsWith('http')) {
    link = event.link;
  } else {
    link = base + event.link;
  }
  if (!event.image) {
    event.image = "/images/events/default.png";
  }
  let options = {
    weekday: 'long',
    year: 'numeric', month: 'numeric', day: 'numeric',
    hour: 'numeric', minute: 'numeric',
    timeZone: 'Europe/Berlin'
  };
  event.begin_string = new Intl.DateTimeFormat('de-DE', options).format(event.begin);
</script>

<Card
  contentRight={false}
  sideImageHalf={true}
  title={event.title}
  subtitle={event.begin_string}
  bigImage={event.image}
  small={true}
  >
  {@html event.description}
</Card>
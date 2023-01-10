<script>
  import EventPreview from '$lib/Events/EventPreview.svelte';
  export let display_events;
</script>

{#each display_events as event, i}
  {#if i % 2 == 0}
    <EventPreview {event} textRight={false} />
  {:else}
    <EventPreview {event} textRight={true} />
  {/if}
{/each}

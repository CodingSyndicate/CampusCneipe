<script>
  import EventPreview from '$lib/Events/EventPreview.svelte';
  export let display_events;
</script>
{#if display_events.length < 1}
  <div class="text-center mt-5">keine bevorstehenden Events</div>
{:else}
  {#each display_events as event, i}
    {#if i % 2 == 0}
      <EventPreview {event} textRight={false} />
    {:else}
      <EventPreview {event} textRight={true} />
    {/if}
  {/each}
{/if}

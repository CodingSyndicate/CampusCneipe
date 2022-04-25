<script>
	import { Nav } from 'svelte-chota';
	import { page } from '$app/stores';
</script>

<Nav>
	<div slot="left">
		<a href="/" class={$page.url.pathname == '/' ? 'active' : ''}><img class="brand" title="Campus Cneipe" src="/favicon.png" alt="Logo" /> CampusCneipe </a>
		<a href="/karte" class={$page.url.pathname.startsWith('/karte') ? 'active' : ''}>Karte</a>
		<a href="/veranstaltungen" class={$page.url.pathname.startsWith('/veranstaltungen') ? 'active' : ''}>Veranstaltungen</a>
		<a href="/neuigkeiten" class={$page.url.pathname.startsWith('/neuigkeiten') ? 'active' : ''}>Neuigkeiten</a>
		<a href="/reservierung" class={$page.url.pathname.startsWith('/reservierung') ? 'active' : ''}>Reservieren</a>
		<a href="/anfahrt" class={$page.url.pathname.startsWith('/anfahrt') ? 'active' : ''}>Anfahrt</a>
	</div>
	<div slot="right">
		<a href="/jobs" class={$page.url.pathname.startsWith('/jobs') ? 'active' : ''}>Jobs</a>
		<a href="/verein" class={$page.url.pathname.startsWith('/verein') ? 'active' : ''}>Verein</a>
		<a href="/intern" class={$page.url.pathname.startsWith('/intern') ? 'active' : ''}>Interner Bereich</a>
	</div>
</Nav>

<style>
	div {
		display: flex;
		flex-direction: row;
	}
	a {
		font-size: larger;
	}
</style>

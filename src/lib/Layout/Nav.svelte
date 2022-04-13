<script>
	import { Nav, Button, Modal, Container } from 'svelte-chota';
	import { page } from '$app/stores';
	import { mdiMenu } from '@mdi/js';
	let width;
	let menu_open = false;
</script>

<svelte:window bind:innerWidth={width} />

<Nav>
	<div slot="left">
		<a sveltekit:prefetch href="/" class={$page.url.pathname == '/' ? 'active' : ''}><img class="brand" title="Campus Cneipe" src="/favicon.png" alt="Logo" /> CampusCneipe </a>
		{#if width >= 768}
			<a sveltekit:prefetch href="/karte" class={$page.url.pathname.startsWith('/karte') ? 'active' : ''}>Karte</a>
			<a sveltekit:prefetch href="/veranstaltungen" class={$page.url.pathname.startsWith('/veranstaltungen') ? 'active' : ''}>Veranstaltungen</a>
			<a sveltekit:prefetch href="/neuigkeiten" class={$page.url.pathname.startsWith('/neuigkeiten') ? 'active' : ''}>Neuigkeiten</a>
			<a sveltekit:prefetch href="/anfahrt" class={$page.url.pathname.startsWith('/anfahrt') ? 'active' : ''}>Anfahrt</a>
		{/if}
	</div>
	<div slot="right" class="rightside">
		{#if width >= 768}
			<a sveltekit:prefetch href="/jobs" class={$page.url.pathname.startsWith('/jobs') ? 'active' : ''}>Jobs</a>
			<a sveltekit:prefetch href="/verein" class={$page.url.pathname.startsWith('/verein') ? 'active' : ''}>Verein</a>
			<a sveltekit:prefetch href="/intern" class={$page.url.pathname.startsWith('/intern') ? 'active' : ''}>Interner Bereich</a>
		{:else}
			<div class="menu">
				<Button primary icon={mdiMenu} on:click={(event) => (menu_open = true)} />
			</div>
		{/if}
	</div>
</Nav>

<Modal bind:open={menu_open}>
	<Container>
		<div class="menucol is-full-screen" on:click={() => (menu_open = false)}>
			<a sveltekit:prefetch href="/" class={$page.url.pathname == '/' ? 'active' : ''}><img class="menubrand" title="Campus Cneipe" src="/favicon.png" alt="Logo" /> CampusCneipe </a>
			<div class="spacer" />
			<a sveltekit:prefetch href="/karte" class={$page.url.pathname.startsWith('/karte') ? 'active' : ''}>Karte</a>
			<a sveltekit:prefetch href="/veranstaltungen" class={$page.url.pathname.startsWith('/veranstaltungen') ? 'active' : ''}>Veranstaltungen</a>
			<a sveltekit:prefetch href="/neuigkeiten" class={$page.url.pathname.startsWith('/neuigkeiten') ? 'active' : ''}>Neuigkeiten</a>
			<a sveltekit:prefetch href="/anfahrt" class={$page.url.pathname.startsWith('/anfahrt') ? 'active' : ''}>Anfahrt</a>
			<a sveltekit:prefetch href="/jobs" class={$page.url.pathname.startsWith('/jobs') ? 'active' : ''}>Jobs</a>
			<a sveltekit:prefetch href="/verein" class={$page.url.pathname.startsWith('/verein') ? 'active' : ''}>Verein</a>
			<a sveltekit:prefetch href="/intern" class={$page.url.pathname.startsWith('/intern') ? 'active' : ''}>Interner Bereich</a>
			<div class="spacer" />
			<a sveltekit:prefetch href="/impressum" class={$page.url.pathname.startsWith('/impressum') ? 'active' : ''}>Impressum</a>
			<a sveltekit:prefetch href="/datenschutz" class={$page.url.pathname.startsWith('/datenschutz') ? 'active' : ''}>Datenschutz</a>
		</div>
	</Container>
</Modal>

<style>
	div {
		display: flex;
		flex-direction: row;
	}
	a {
		font-size: larger;
	}
	.menu {
		display: flex;
		justify-content: center;
		align-items: center;
		padding-right: 1rem;
	}
	.menucol {
		display: flex;
		flex-direction: column;
		background-color: #000000;
		align-items: center;
		padding-top: 8rem;
	}
	.menucol > a {
		line-height: 3;
	}
	.menubrand {
		width: 4rem;
		height: 4rem;
	}
	.spacer {
		height: 2rem;
	}
	@media (max-width: 768px) {
		.rightside {
			justify-self: center;
		}
	}
</style>

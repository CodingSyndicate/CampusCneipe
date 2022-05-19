<script>
	import { mdiHeart, mdiCopyright } from '@mdi/js';
	import { Icon } from 'svelte-chota';
</script>

<footer class="footerContainer">
	<div class="left"><Icon src={mdiCopyright} size="24px" /> 2022 - Campus Cneipe</div>
	<div class="middle">
		<div class="impressum">
			<a sveltekit:prefetch href="/impressum">Impressum</a>
			&nbsp;
			<a href="https://github.com/CodingSyndicate/CampusCneipe"> 0.2.1 </a>
			&nbsp;
			<a sveltekit:prefetch href="/datenschutz">Datenschutz</a>
		</div>
	</div>
	<div class="right">
		Made with &nbsp; <Icon src={mdiHeart} size="24px" color="red" />&nbsp; by &nbsp;<a href="https://github.com/CodingSyndicate">Coding-Syndicate</a>
	</div>
</footer>

<style>
	.footerContainer {
		display: flex;
		flex-direction: row;
		width: 100%;
		margin: 0;
		padding-top: 5px;
		padding-bottom: 5px;
		background-color: #222222;
		color: white;
		justify-content: center;
		align-items: center;
	}
	.middle {
		width: 33%;
		display: flex;
		flex-direction: row;
		justify-content: space-evenly;
		align-items: center;
	}
	.left {
		width: 33%;
		display: flex;
		justify-content: flex-start;
		align-items: center;
	}
	.right {
		width: 33%;
		display: flex;
		justify-content: flex-end;
		align-items: center;
	}
	a {
		color: white;
	}
	@media (max-width: 768px) {
		.footerContainer {
			flex-direction: column;
		}
		.footerContainer > div {
			width: 100%;
			justify-content: center;
			line-height: 2.5;
		}
	}
</style>

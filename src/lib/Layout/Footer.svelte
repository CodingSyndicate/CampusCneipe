<script>
	import { mdiHeart, mdiCopyright } from '@mdi/js';
	import { Icon } from 'svelte-chota';
</script>

<footer class="footerContainer">
	<div class="left"><Icon src={mdiCopyright} size="24px" /> 2022 - Campus Cneipe</div>
	<div class="middle">
		<div class="impressum">
			<a href="/impressum">Impressum</a>
			&nbsp;
			<a href="https://github.com/CodingSyndicate/CampusCneipe">0.0.2</a>
			&nbsp;
			<a href="/datenschutz">Datenschutz</a>
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
	}
	.right {
		width: 33%;
		display: flex;
		justify-content: flex-end;
		align-items: center;
	}
</style>

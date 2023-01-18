<script>
  import { page } from '$app/stores';
  import { base } from '$app/paths';
  export let compileTime;
  export let modificationTime;
</script>

<footer class="col">
	<a href="{base}/" class="logoCon navbar-brand" />
	<hr />
	<div class="actions row">
		<div class="col">
			<img src="{base}/svg/glass-mug-variant.svg" alt="Karte" />
			<a
				sveltekit:prefetch
				href="{base}/karte"
				class="nav-link"
				class:active={$page.url.pathname.startsWith('/karte')}
				aria-current={$page.url.pathname.startsWith('/karte') ? 'page' : ''}
			>
				KARTE
			</a>
		</div>
		<div class="col">
			<img src="{base}/svg/nightlife.svg" alt="Events" />
			<a
				sveltekit:prefetch
				href="{base}/events"
				class="nav-link"
				class:active={$page.url.pathname.startsWith('/events')}
				aria-current={$page.url.pathname.startsWith('/events') ? 'page' : ''}
			>
				EVENTS
			</a>
		</div>
		<div class="col">
			<div class="col">
				<img src="{base}/svg/celebration.svg" alt="Mieten" />
				<a
					sveltekit:prefetch
					href="{base}/mieten"
					class="nav-link"
					class:active={$page.url.pathname.startsWith('/mieten')}
					aria-current={$page.url.pathname.startsWith('/mieten') ? 'page' : ''}
				>
					MIETEN
				</a>
			</div>
		</div>
	</div>
	<hr />
	<!-- <div class="lastLine"> -->
	<!-- <\!-- 	<span class="text-left">© &nbsp; 2022 - Campus Cneipe</span> -\-> -->
	<!-- 	<span class="text-center"> -->
	<!-- 	  Contribute on <a href="https://github.com/CodingSyndicate/CampusCneipe"> Github </a> -->
	<!-- 	</span> -->
	<!-- 	<\!-- <span class="text-right"> -\-> -->
	<!-- 	<\!-- 	Made with ❤ by &nbsp; -\-> -->
	<!-- 	<\!-- 	<a href="https://github.com/GeneralMine">GeneralMine</a> -\-> -->
	<!-- 	<\!-- </span> -\-> -->
	<!-- </div> -->
	<div class="lastUpdated">
	  <span style="font-size: 14px;">contribute on <a href="https://github.com/CodingSyndicate/CampusCneipe"> Github </a> |
	    last deploy: {compileTime} |
	    last modification: {modificationTime}
	  </span>
	</div>
</footer>

<style>
	footer {
		width: calc(100% - 320px);
		margin-left: 320px;
		display: flex;
		flex-direction: column;
		justify-content: center;
		align-items: center;
		margin-top: 2.5rem;
		margin-bottom: 2.5rem;
	}
	.col {
		display: flex;
		flex-direction: column;
		justify-content: center;
		align-items: center;
	}
	.row {
		display: flex;
		flex-direction: row;
		justify-content: space-around;
		align-items: center;
	}
	.actions {
		margin-bottom: 2.5rem;
		margin-top: 2.5rem;
		width: 60%;
	}
	hr {
		background-color: #5d646b;
		width: 90%;
		height: 2px;
		opacity: 1;
		border: none;
	}
	.logoCon {
		min-height: 78px;
		min-width: 250px;
		margin-bottom: 2.5rem;
		background-image: url('/images/LogoWebsiteHorizontalLong.png');
		background-repeat: no-repeat;
		background-position: center;
	}
	img {
		width: 32px;
		height: 32px;
		margin-bottom: 2rem;
	}
	.active {
		color: var(--bs-primary);
	}
	a {
		color: #bfbfbf;
		text-decoration: none;
		--bs-navbar-hover-color: var(--bs-primary);
	}
	a:hover {
		color: var(--bs-primary);
	}
	.lastLine {
		width: 80%;
		display: flex;
		flex-direction: row;
		justify-content: space-between;
		align-items: center;
		margin-top: 2.5rem;
	}
	.lastLine > span {
		width: 222px;
	}
	.lastLine > span > a {
		text-decoration: dotted underline;
	}
	@media (max-width: 992px) {
		footer {
			width: 100%;
			margin-left: 0;
		}
		.lastLine {
			width: 90%;
		}
	}
	@media (max-width: 800px) {
		footer {
			width: 100%;
			margin-left: 0;
		}
		.lastLine {
			flex-direction: column-reverse;
		}
		.lastLine > span {
			width: 100%;
			text-align: center;
			line-height: 2;
		}
	}
</style>

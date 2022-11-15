<script>
	import { page } from '$app/stores';
	import { goto } from '$app/navigation';
	import { base } from '$app/paths';
	let collapsed = true;
	$: show = !collapsed;

	function navigate(dest) {
		collapsed = !collapsed;
		goto(base + dest);
	}
</script>

<nav class="navbar navbar-expand-lg navbar-dark">
	<div class="container-fluid">
		<a href="{base}/" class="logoCon navbar-brand m-0" />

		<button
			class:collapsed
			class="navbar-toggler"
			type="button"
			data-bs-toggle="collapse"
			data-bs-target="#navbarNav"
			aria-controls="navbarNav"
			aria-expanded="false"
			aria-label="Toggle navigation"
			on:click={() => (collapsed = !collapsed)}
		>
			<span class="navbar-toggler-icon" />
		</button>

		<div class:show class="collapse navbar-collapse" id="navbarNav">
			<ul class="navbar-nav">
				<li class="nav-item text-center first">
					<a
						sveltekit:prefetch
						href="{base}/"
						class="nav-link"
						class:active={$page.url.pathname === base + '/'}
						aria-current={$page.url.pathname === base + '/' ? 'page' : ''}
						on:click={() => navigate('/')}
					>
						HOME
					</a>
				</li>
				<li class="nav-item  text-center">
					<a
						sveltekit:prefetch
						href="{base}/karte"
						class="nav-link"
						class:active={$page.url.pathname.startsWith(base + '/karte')}
						aria-current={$page.url.pathname.startsWith(base + '/karte') ? 'page' : ''}
						on:click={() => navigate('/karte')}
					>
						KARTE
					</a>
				</li>
				<li class="nav-item  text-center">
					<a
						sveltekit:prefetch
						href="{base}/events"
						class="nav-link"
						class:active={$page.url.pathname.startsWith(base + '/events')}
						aria-current={$page.url.pathname.startsWith(base + '/events') ? 'page' : ''}
						on:click={() => navigate('/events')}
					>
						EVENTS
					</a>
				</li>
				<li class="nav-item  text-center">
					<a
						sveltekit:prefetch
						href="{base}/mieten"
						class="nav-link"
						class:active={$page.url.pathname.startsWith(base + '/mieten')}
						aria-current={$page.url.pathname.startsWith(base + '/mieten') ? 'page' : ''}
						on:click={() => navigate('/mieten')}
					>
						MIETEN
					</a>
				</li>
				<li class="nav-item  text-center">
					<a
						sveltekit:prefetch
						href="{base}/mitmachen"
						class="nav-link"
						class:active={$page.url.pathname.startsWith(base + '/mitmachen')}
						aria-current={$page.url.pathname.startsWith(base + '/mitmachen') ? 'page' : ''}
						on:click={() => navigate('/mitmachen')}
					>
						MITMACHEN
					</a>
				</li>
				<li class="nav-item  text-center">
					<a
						sveltekit:prefetch
						href="{base}/kontakt"
						class="nav-link"
						class:active={$page.url.pathname.startsWith(base + '/kontakt')}
						aria-current={$page.url.pathname.startsWith(base + '/kontakt') ? 'page' : ''}
						on:click={() => navigate('/kontakt')}
					>
						KONTAKT
					</a>
				</li>
			</ul>
			<div class="socialmediaContainer">
				<div class="socialmediaList row align-items-center justify-content-center">
					<a
						class="btn btn-primary btn-lg btn-floating socialmediabutton"
						role="button"
						href="https://www.instagram.com/campus_cneipe/"
					>
						<img
							src="{base}/svg/instagram.svg"
							alt="Instagram"
							style="height: 24px; width: 24px; margin:0;"
						/>
					</a>
					<a
						class="btn btn-primary btn-lg btn-floating socialmediabutton"
						role="button"
						href="https://twitter.com/campuscneipe"
					>
						<img
							src="{base}/svg/twitter.svg"
							alt="Twitter"
							style="height: 24px; width: 24px; margin:0;"
						/>
					</a>
					<a
						class="btn btn-primary btn-lg btn-floating socialmediabutton"
						role="button"
						href="https://www.facebook.com/campuscneipe/"
					>
						<img
							src="{base}/svg/facebook.svg"
							alt="Facebook"
							style="height: 24px; width: 24px; margin:0;"
						/>
					</a>
					<a
						class="btn btn-primary btn-lg btn-floating socialmediabutton"
						role="button"
						href="{base}/"
					>
						<img src="{base}/svg/rss.svg" alt="" style="height: 24px; width: 24px; margin:0;" />
					</a>
				</div>
			</div>
			<ul class="impressum-datenschutz navbar-nav">
				<li class="nav-item text-center">
					<a
						sveltekit:prefetch
						href="{base}/impressum"
						class="nav-link"
						class:active={$page.url.pathname.startsWith(base + '/impressum')}
						aria-current={$page.url.pathname.startsWith(base + '/impressum') ? 'page' : ''}
						on:click={() => (collapsed = true)}
					>
						IMPRESSUM
					</a>
				</li>
				<li class="nav-item text-center">
					<a
						sveltekit:prefetch
						href="{base}/datenschutz"
						class="nav-link"
						class:active={$page.url.pathname.startsWith(base + '/datenschutz')}
						aria-current={$page.url.pathname.startsWith(base + '/datenschutz') ? 'page' : ''}
						on:click={() => (collapsed = true)}
					>
						DATENSCHUTZ
					</a>
				</li>
			</ul>
		</div>
	</div>
</nav>

<style>
	nav {
		position: fixed;
		z-index: 10;
		height: 100vh;
		width: 320px;
		background-color: #282b2f;
		letter-spacing: 0.015em;
		border-right: 2px solid #273489;
		padding: 0;
		font-family: 'Unica One', Lato, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto,
			'Helvetica Neue', Arial, sans-serif, 'Apple Color Emoji', 'Segoe UI Emoji', 'Segoe UI Symbol';
	}
	.logoCon {
		padding: 60px;
		height: 320px;
		width: 312px;
		min-height: 260px;
		min-width: 252px;
		background-image: url('/images/LogoWebsite.png');
		background-repeat: no-repeat;
		background-position: center;
	}
	.container-fluid {
		padding: 0;
		width: 100%;
		height: 100%;
		flex-direction: column;
		justify-content: space-between;
		align-items: center;
	}
	.socialmediaContainer {
		width: 100%;
	}
	.socialmediabutton {
		background-color: #313539;
		border: 1px solid #282b2f;
		border-radius: 50%;
		width: 34px;
		height: 34px;
		display: flex;
		align-items: center;
		justify-content: center;
		padding: 8px;
		margin: 5px;
		line-height: 18px;
		opacity: 0.6;
		transition: opacity 0.2s;
	}
	.socialmediabutton:hover {
		opacity: 1;
	}
	ul {
		width: 100%;
		background-color: #282b2f;
		display: flex;
		flex-direction: column;
	}
	li {
		border-bottom-width: 1px;
		border-bottom-style: solid;
		border-color: #313539;
		height: 57px;
		font-size: 18px;
		letter-spacing: 0.015em;
		line-height: 36px;
		width: 100%;
	}
	li > a {
		width: 100%;
		height: 100%;
		display: flex;
		align-items: center;
		justify-content: center;
	}
	.first {
		border-top: 1px solid #313539;
	}
	.collapse {
		flex-direction: column;
		width: 100%;
	}
	.impressum-datenschutz {
		flex-direction: row;
		/* border-top: 1px solid #313539; */
	}
	.impressum-datenschutz > li {
		border-bottom: none;
		font-size: 14px;
		line-height: 30px;
		height: 50px;
	}
	#navbarNav {
		flex-direction: column;
		justify-content: space-between;
		--bs-navbar-hover-color: var(--bs-primary);
	}
	.active {
		color: var(--bs-primary);
	}
	.navbar-toggler {
		padding: 0.5rem !important;
	}
	@media (max-width: 992px) {
		nav {
			height: 108px;
			width: 100%;
			flex-direction: row;
			align-content: space-between;
			justify-content: center;
			padding-top: 15px;
			padding-bottom: 15px;
			padding-right: 25px;
			padding-left: 25px;
			border-right: none;
			border-bottom: 2px solid var(--bs-primary);
			background-color: #282b2f;
		}
		.container-fluid {
			flex-direction: row;
			justify-content: space-between;
			align-items: center;
		}
		.logoCon {
			padding: 0;
			height: 78px;
			width: 250px;
			min-height: 78px;
			min-width: 250px;
			background-image: url('/images/LogoWebsiteHorizontalLong.png');
		}
		#navbarNav {
			background-color: #282b2f;
		}
		.socialmediaList {
			padding: 0;
			display: flex;
			justify-content: center;
			align-items: center;
			padding-top: 1rem;
			padding-bottom: 0.5rem;
		}
	}
	@media (max-width: 370px) {
		.logoCon {
			background-image: url('/images/LogoWebsiteHorizontal.png');
			background-position: left;
			width: 190px;
			min-width: 190px;
		}
	}
	@media (max-width: 294px) {
		nav {
			padding-left: 0;
			padding-right: 0;
		}
		.navbar-toggler {
			margin: 0 auto;
		}
	}
	@media (max-height: 692px) {
		.logoCon {
			min-width: auto;
			min-height: auto;
		}
		.nav-link {
			padding: 0;
		}
		.nav-item {
			height: 40px;
		}
	}
	@media (max-height: 520px) {
		.logoCon {
			background-image: url('/images/LogoWebsiteHorizontal.png');
		}
	}
	@media (max-height: 520px) {
		.logoCon {
			max-width: 100%;
			max-height: 100%;
			padding: 0;
		}
		#navbarNav {
			min-height: 334px;
		}
	}
</style>

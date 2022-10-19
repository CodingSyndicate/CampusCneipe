<div class="block">
	<div class="co">
		<h2>Wir sind zurück aus den Semesterferien!</h2>
		<h4>Wiedereröffnungsfeier: 24.10.2022 15 Uhr</h4>
		<span>Freibier ab 16 Uhr und TUM-Präsident Hofmann als Ehrengast!</span>
	</div>
</div>

<style>
	.block {
		position: relative;
		z-index: 10;
		margin: 100px auto 0;
		background: linear-gradient(0deg, #000, #272727);
	}

	.co {
		background-color: rgba(0, 0, 0, 0.8);
		width: 100%;
		height: 100%;
		padding: 1rem;
		display: flex;
		flex-direction: column;
		justify-content: center;
		align-items: center;
		text-align: center;
	}
	.block:before,
	.block:after {
		content: '';
		position: absolute;
		left: -2px;
		top: -2px;
		background: linear-gradient(45deg, #fb0094, #0000ff, #00ff00, #ffff00, #ff0000, #fb0094, #0000ff, #00ff00, #ffff00, #ff0000);
		background-size: 400%;
		width: calc(100% + 4px);
		height: calc(100% + 4px);
		z-index: -1;
		animation: steam 20s linear infinite;
	}

	@keyframes steam {
		0% {
			background-position: 0 0;
		}
		50% {
			background-position: 400% 0;
		}
		100% {
			background-position: 0 0;
		}
	}

	.block:after {
		filter: blur(50px);
	}
</style>

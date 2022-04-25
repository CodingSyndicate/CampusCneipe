<script context="module">
	export async function load({ url }) {
		return {
			status: 301,
			redirect: 'https://www.c2.tum.de'
		};
	}
</script>

<slot />

<script>
	import { goto } from '$app/navigation';

	import KartenKategorie from '$lib/Karte/KartenKategorie.svelte';
	import { Button } from 'svelte-chota';

	let loading = true;

	let data = [
		{
			name: 'Bier & Wein',
			image: 'https://images.unsplash.com/photo-1518791841217-8f162f1e1131?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=800&q=60',
			type: 'drinks',
			color: '#3B1304',
			content: [
				{
					name: 'Helles',
					subtitle: 'vom Fass',
					description: 'auch Alkoholfrei',
					amount: '0,5l / 1,0l',
					price: '3,30 / 6,10'
				},
				{
					name: 'Weißbier',
					subtitle: 'vom Fass',
					description: 'auch Alkoholfrei',
					amount: '0,5l',
					price: '3,30'
				},
				{
					name: 'Vitus',
					subtitle: 'vom Fass',
					description: null,
					amount: '0,5l',
					price: '3,50'
				},
				{
					name: 'Helles',
					subtitle: null,
					description: null,
					amount: '0,5l',
					price: '3,30'
				},
				{
					name: 'Dunkles Weißbier',
					subtitle: null,
					description: null,
					amount: '0,5l',
					price: '3,30'
				},
				{
					name: 'Pils',
					subtitle: null,
					description: null,
					amount: '0,33l',
					price: '2,90'
				},
				{
					name: 'Radler',
					subtitle: null,
					description: null,
					amount: '0,5l / 1,0l',
					price: '3,30 / 6,10'
				},
				{
					name: 'Russn / Colaweizen',
					subtitle: null,
					description: null,
					amount: '0,5l',
					price: '3,30'
				},
				{
					name: 'Isarwasser',
					subtitle: null,
					description: null,
					amount: '0,5l',
					price: '4,20'
				},
				{
					name: 'Vitusse',
					subtitle: null,
					description: null,
					amount: '0,5l',
					price: '3,50'
				},
				{
					name: 'Goaßmaß',
					subtitle: null,
					description: null,
					amount: '1,0l',
					price: '6,60'
				}
			]
		},
		{
			name: 'Classics',
			image: 'https://images.unsplash.com/photo-1518791841217-8f162f1e1131?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=800&q=60',
			type: 'drinks',
			color: '#17567A',
			content: [
				{
					name: 'Fresh Hermann',
					subtitle: null,
					description: 'Der TUM Klassiker',
					amount: '0,5l',
					price: '6,30'
				},
				{
					name: 'Tequila Sunrise',
					subtitle: null,
					description: 'Tequila, Zitronensaft, Orangensaft, Grenadine',
					amount: '-',
					price: '6,30'
				},
				{
					name: 'Caipirinha',
					subtitle: null,
					description: 'Limette, Rohrzucker, Cachaca, Soda',
					amount: '-',
					price: '6,30'
				},
				{
					name: 'Touch Down',
					subtitle: null,
					description: 'Vodka, Apricot, Brandy, Zitronensaft, Grenadine, Maracujanektar',
					amount: '-',
					price: '6,30'
				},
				{
					name: 'Sex on the Beach',
					subtitle: null,
					description: 'Vodka, Pfirsichlikör, Orangensaft, Cranberrynektar',
					amount: '-',
					price: '6,30'
				},
				{
					name: 'Mojito',
					subtitle: null,
					description: 'Limette, Rohrzucker, Havana Club Rum, Minze, Soda',
					amount: '-',
					price: '6,30'
				},
				{
					name: 'Negroni',
					subtitle: null,
					description: 'Gin, Campari, Vermouth',
					amount: '-',
					price: '6,30'
				},
				{
					name: 'Pina Colada',
					subtitle: null,
					description: 'Cream of Coconut, Ananassaft, Maracujanektar, dunkler Rum',
					amount: '-',
					price: '6,30'
				}
			]
		},
		{
			name: 'Longdrinks Light',
			image: 'https://images.unsplash.com/photo-1518791841217-8f162f1e1131?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=800&q=60',
			type: 'drinks',
			color: '#4F2456',
			content: [
				{
					name: 'Vodka Bull',
					subtitle: null,
					description: 'Absolut Vodka, Red Bull',
					amount: '-',
					price: '7,60'
				},
				{
					name: 'Cuba Libre',
					subtitle: null,
					description: 'Havanna Club Rum, Limette, Coca Cola',
					amount: '-',
					price: '5,90'
				},
				{
					name: 'Gin Tonic',
					subtitle: null,
					description: 'Bombay Saphire Gin, Tonic Water',
					amount: '-',
					price: '6,30'
				},
				{
					name: 'Moscow oder Munich Mule',
					subtitle: null,
					description: 'Vodka oder Gin, Limettensaft, Gingerbeer',
					amount: '-',
					price: '6,30'
				}
			]
		},
		{
			name: 'Longdrinks Strong',
			image: 'https://images.unsplash.com/photo-1518791841217-8f162f1e1131?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=800&q=60',
			type: 'drinks',
			color: '#155E4C',
			content: [
				{
					name: 'Long Island Iced Tea',
					subtitle: null,
					description: 'heller Rum, Vodka, Bombay Gin, Cointreau, Zitronensaft, Rohrzuckersirup, Coca Cola',
					amount: '-',
					price: '7,60'
				},
				{
					name: 'Zombie',
					subtitle: null,
					description: 'dunkler Rum, heller Rum, Limettensaft, Apricot Brandy, Grenadine, Orangensaft, Ananassaft',
					amount: '-',
					price: '7,60'
				},
				{
					name: 'Mai Tai',
					subtitle: null,
					description: 'dunkler Rum, heller Rum, Limettensaft, Cointreau, Mandelsirup, Rohrzuckersirup',
					amount: '-',
					price: '7,60'
				}
			]
		},
		{
			name: 'Softdrinks & co.',
			image: 'https://images.unsplash.com/photo-1518791841217-8f162f1e1131?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=800&q=60',
			type: 'drinks',
			color: '#700505',
			content: [
				{
					name: 'Säfte / Nektar',
					subtitle: null,
					description: 'Apfel, Ananas, Orange, Johannesbeere, Maracuja',
					amount: '0,4l',
					price: '2,90'
				},
				{
					name: 'Saftschorlen',
					subtitle: null,
					description: 'Apfel, Ananas, Orange, Johannesbeere, Maracuja',
					amount: '0,5l',
					price: '2,90'
				},
				{
					name: 'Zitronenlimonade',
					subtitle: null,
					description: null,
					amount: '0,5l',
					price: '2,40'
				},
				{
					name: 'Colamix',
					subtitle: null,
					description: null,
					amount: '0,5l',
					price: '2,60'
				},
				{
					name: 'Clubmate',
					subtitle: null,
					description: null,
					amount: '0,5l',
					price: '2,90'
				},
				{
					name: 'Cola',
					subtitle: null,
					description: null,
					amount: '0,4l',
					price: '2,60'
				},
				{
					name: 'Tafelwasser',
					subtitle: null,
					description: null,
					amount: '0,5l',
					price: '2,40'
				},
				{
					name: 'Red Bull',
					subtitle: null,
					description: null,
					amount: '0,33l',
					price: '3,40'
				},
				{
					name: 'Schweppes',
					subtitle: null,
					description: 'Ginger Ale, Ginger Beer, Tonic Water',
					amount: '0,5l',
					price: '2,30'
				},
				{
					name: 'Heiße Getränke',
					subtitle: null,
					description: 'Kaffee, Heiße Zitrone, Tee',
					amount: '-',
					price: '2,90'
				}
			]
		},
		{
			name: 'Sprizz',
			image: 'https://images.unsplash.com/photo-1518791841217-8f162f1e1131?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=800&q=60',
			type: 'drinks',
			color: '#0D4710',
			content: [
				{
					name: 'Aperol Sprizz',
					subtitle: null,
					description: 'Aperol, Prosecco, Soda',
					amount: '-',
					price: '4,60'
				},
				{
					name: 'Limoncello Sprizz',
					subtitle: null,
					description: 'Limoncello, Prosecco, Soda',
					amount: '-',
					price: '4,60'
				},
				{
					name: "Pimm's Cup",
					subtitle: null,
					description: "Pimm's No 1, Ginger Ale",
					amount: '-',
					price: '6,30'
				}
			]
		},
		{
			name: 'Fizzes & Sours',
			image: 'https://images.unsplash.com/photo-1518791841217-8f162f1e1131?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=800&q=60',
			type: 'drinks',
			color: '#33234D',
			content: [
				{
					name: 'Gin Basil Smash',
					subtitle: null,
					description: 'Basilikum, Gin, Zitronensaft',
					amount: '-',
					price: '6,30'
				},
				{
					name: 'Fizz',
					subtitle: null,
					description: 'Spirit, Zitronensaft, Rohrzuckersirup, Soda',
					amount: '-',
					price: '6,30'
				},
				{
					name: 'Sour',
					subtitle: null,
					description: 'Spirit, Zitronensaft, Rohrzuckersirup',
					amount: '-',
					price: '6,30'
				}
			]
		},
		{
			name: 'Mocktails',
			image: 'https://images.unsplash.com/photo-1518791841217-8f162f1e1131?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=800&q=60',
			type: 'drinks',
			color: '#40099A',
			content: [
				{
					name: 'Ginger Basil Smash',
					subtitle: null,
					description: 'Basilikum, Grapefruitsaft, Gingerbeer',
					amount: '-',
					price: '5,30'
				},
				{
					name: 'Mint Tonic',
					subtitle: null,
					description: 'Rohrzuckersirup, Zitrone, Minzzweig, Tonic Water',
					amount: '-',
					price: '5,30'
				},
				{
					name: 'Crodino Ale | Ginger Fizz',
					subtitle: null,
					description: 'Crodino, Ginger Ale | Ginger Beer, Soda',
					amount: '-',
					price: '6,30'
				},
				{
					name: 'Caipinino',
					subtitle: null,
					description: 'Crodino, Ginger Ale | Ginger Beer, Soda',
					amount: '-',
					price: '5,30'
				},
				{
					name: 'PiNADA Colada',
					subtitle: null,
					description: 'Cream of Coconut, Ananassaft, Maracujanektar, Limettensaft',
					amount: '-',
					price: '5,30'
				}
			]
		}
	];
</script>

<svelte:head>
	<title>Karte | CampusCneipe</title>
	<meta name="description" content="Karte aller Getränke und Speisen der Campus Cneipe" />
	<meta property="og:title" content="Getränkekarte der Campus Cneipe" />
	<meta property="og:image" content="https://www.c2.tum.de/images/Hintergrundbild.jpg" />
	<meta property="og:url" content="https://www.c2.tum.de/" />
	<meta property="og:site_name" content="Getränkekarte der Campus Cneipe" />
	<meta property="og:description" content="Karte aller Getränke und Speisen der Campus Cneipe" />
</svelte:head>

<img class="background" src="./images/Hintergrundbilder.png" alt="Bild der Cneipe" />

<div class="myrow" />

{#each data as category, i}
	{#if i % 2 === 0}
		<KartenKategorie {category} />
	{:else}
		<KartenKategorie {category} otherside={true} />
	{/if}
{/each}

<div class="pdf">
	<Button primary on:click={() => goto('/karte.pdf')}>Download als PDF</Button>
</div>

<style>
	.background {
		width: 100%;
		height: 100%;
		object-fit: contain;
	}
	.pdf {
		display: flex;
		justify-content: center;
		align-items: center;
		padding: 1em;
	}
</style>

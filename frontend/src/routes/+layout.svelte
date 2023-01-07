<script>
	import Header from '$lib/Header.svelte';
	import Footer from '$lib/Footer.svelte';
	import NavBar from '$lib/NavBar.svelte';
	import Exercises from '$lib/Exercises.svelte';
	import Subtitle from '$lib/Subtitle.svelte'
	import './styles.css';

	let search;
	let result_exercises = [];

	async function update_search(value) {
		if (value && value.trim().length > 0) {
			result_exercises = await fetch(`/search?q=${value.trim()}`).then((v) => v.json());
		} else {
			result_exercises = [];
		}
	}
	$: update_search(search);
</script>

<div class="app">
	<Header bind:search/>
	
	{#if search}
		{#if result_exercises.length !== 0}
			<Exercises on:click={() => {search = ""}} search={search} subtitle="Results" exercises={result_exercises} />
		{:else}
			<Subtitle text="No results" />
		{/if}
	{:else}
		<NavBar />
		<slot />
	{/if}

	<div style="height: 30px;"></div>
	<Footer/>
</div>
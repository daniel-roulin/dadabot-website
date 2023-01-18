<script>
	import Header from '$lib/Header.svelte';
	import Footer from '$lib/Footer.svelte';
	import NavBar from '$lib/NavBar.svelte';
	import Exercises from '$lib/Exercises.svelte';
	import Subtitle from '$lib/Subtitle.svelte'
	import './styles.css';

	import { queryParam } from "sveltekit-search-params";
	import { page } from '$app/stores';
	
	let search = queryParam("search");
	let result_exercises_promise;
	update_search();

	function update_search() {
		let value = $search
		if (value && value.trim().length > 0) {
			result_exercises_promise = fetch_search_results(value);
		}
	}

	async function fetch_search_results(value) {
		let res = await fetch(`/search?q=${value.trim()}`);
		return await res.json();
	}
</script>

<div class="app">
	<Header bind:search={$search} on:input={update_search}/>
	
	{#if $search && $search.trim().length > 0}
		{#await result_exercises_promise}
			<Subtitle text="Loading..." />
		{:then results} 
			{#if results.length !== 0}
				<Exercises search={$search} subtitle="Results" exercises={results} />
			{:else}
				<Subtitle text="No results" />
			{/if}
		{/await}
	{:else}
		<NavBar />
		<slot />
	{/if}

	<div style="height: 30px;"></div>
	<Footer/>
</div>
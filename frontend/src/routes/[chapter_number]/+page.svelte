<script>
    export let data

	import NavBar from "$lib/NavBar.svelte";
    import Exercise from "$lib/Exercise.svelte";

    
</script>

<svelte:head>
	<title>Chapter {data.chapter_number}</title>
	<meta name="description" content="Exercises of chapter {data.chapter_number}" />
</svelte:head>

<NavBar chapter={data.chapter_number} />
<h2 class="subtitle-text">
    <a href="/">Recent</a>
</h2>
{#each data.exercises as exercise, index}
    <Exercise {...exercise} />
    {#if !(index == data.exercises.length-1)}
        <hr class="exercise-divider">
    {/if}
{/each}

<style>
.exercise-divider {
    margin: 0px 10px;
    border: 1px solid var(--secondary2);
}

h2 {
    /* position: sticky;
    top: 80px; */
    margin: 10px;
    margin-top: 20px;
    margin-bottom: 15px;
    font-weight: 400;
    font-size: 20px;
    /* background-color: var(--background1); */
}
</style>
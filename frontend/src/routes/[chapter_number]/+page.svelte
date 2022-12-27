<script>
    export let data

	import NavBar from "../NavBar.svelte";
    import Exercise from "./Exercise.svelte";
</script>

<svelte:head>
	<title>Chapter {data.chapter_number}</title>
	<meta name="description" content="Exercises of chapter {data.chapter_number}" />
</svelte:head>

<NavBar chapter={data.chapter_number} />
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
</style>
<script>
	import { onMount } from "svelte"; 
	import NavBar from "$lib/NavBar.svelte";
    import Exercise from "$lib/Exercise.svelte";
    import Subtitle from "$lib/Subtitle.svelte"; 
    import { setRecentExercise, getRecentExercises } from "$lib/recent.ts"

    export let data


    $: recent = {exercises: []};
    onMount(() => {
        recent = {exercises: getRecentExercises()};
    });
</script>

<svelte:head>
	<title>Chapter {data.chapter_number}</title>
	<meta name="description" content="Exercises of chapter {data.chapter_number}" />
</svelte:head>


<NavBar chapter={data.chapter_number} />

{#if (recent.exercises.length != 0)}
    <Subtitle text="Recent" />
    {#each recent.exercises as exercise_data, index}
        <Exercise on:click={() => setRecentExercise(exercise_data)} {...exercise_data} />
        {#if !(index == recent.exercises.length-1)}
            <hr class="exercise-divider">
        {/if}
    {/each}
{/if}

<Subtitle text="All" />
{#each data.exercises as exercise_data, index}
    <Exercise on:click={() => setRecentExercise(exercise_data)} {...exercise_data} />
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
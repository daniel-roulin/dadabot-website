<script>
	import { onMount } from "svelte"; 
	import NavBar from "$lib/NavBar.svelte";
    import Exercise from "$lib/Exercise.svelte";
    import Subtitle from "$lib/Subtitle.svelte"; 
    import { setRecentExercise, getRecentExercises } from "$lib/recent.js"

    export let data;

    let all_exercises = data.exercises;
    $: recent_exercises = [];
    onMount(async () => {
        recent_exercises = getRecentExercises();
    });
</script>

<svelte:head>
	<title>Chapter {data.chapter}</title>
	<meta name="description" content="Exercises of chapter {data.chapter}" />
</svelte:head>


<NavBar />

<!-- Idea: Exercises component: name="All", exercises="all_exercises" -->
{#if (recent_exercises.length != 0)}
    <Subtitle text="Recent" />
    {#each recent_exercises as exercise, index}
        <Exercise on:click={() => setRecentExercise(exercise)} {...exercise} />
        {#if !(index === recent_exercises.length-1)}
            <hr class="exercise-divider">
        {/if}
    {/each}
{/if}

<Subtitle text="All" />
{#each all_exercises as exercise, index}
    <Exercise on:click={() => setRecentExercise(exercise)} {...exercise} />
    {#if !(index === all_exercises.length-1)}
        <hr class="exercise-divider">
    {/if}
{/each}


<style>
.exercise-divider {
    margin: 0px 10px;
    border: 1px solid var(--secondary2);
}
</style>
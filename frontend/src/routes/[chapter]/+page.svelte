<script>
	import { onMount } from "svelte"; 
    import Exercises from "$lib/Exercises.svelte";
    import { getRecentExercises } from "$lib/recent.js"

    export let data;

    let all_exercises = data.all_exercises;
    let trending_exercises = data.trending_exercises;
    $: recent_exercises = [];
    onMount(async () => {
        recent_exercises = getRecentExercises(data.chapter);
    });
</script>

<svelte:head>
	<title>Chapter {data.chapter}</title>
	<meta name="description" content="Exercises of chapter {data.chapter}" />
</svelte:head>

<Exercises subtitle="Recent" exercises={recent_exercises}/>
<Exercises subtitle="Trending" exercises={trending_exercises}/>
<Exercises subtitle="All" exercises={all_exercises}/>
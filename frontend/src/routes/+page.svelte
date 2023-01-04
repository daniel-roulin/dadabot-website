<script>
	import Chapters from "$lib/Chapters.svelte";
	import { onMount } from "svelte";
    import { getRecentChapters } from "$lib/recent.js"

    export let data;

    let all_chapters = data.chapters;
    $: recent_chapters = [];
    onMount(async () => {
        recent_chapters = getRecentChapters();
    });
</script>

<svelte:head>
	<title>Dadabot</title>
	<meta name="description" content="Dadabot: Never do your physics homework again!" />
</svelte:head>

{#if (recent_chapters.length !== 0)}
    <Chapters subtitle="Recent" chapters={recent_chapters} />
{/if}

<Chapters subtitle="All" chapters={all_chapters} />

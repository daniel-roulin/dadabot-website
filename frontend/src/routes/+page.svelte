<script>
	import Chapter from "$lib/Chapter.svelte";
    import NavBar from "$lib/NavBar.svelte";
    import Subtitle from "$lib/Subtitle.svelte";
	import { onMount } from "svelte"; 
    import { getRecentChapters, setRecentChapter } from "$lib/recent.ts"

    export let data;

    $: recent = {chapters: []};
    onMount(() => {
        recent = {chapters: getRecentChapters()};
    });
</script>

<svelte:head>
	<title>Dadabot</title>
	<meta name="description" content="Dadabot: Never do your physics homework again!" />
</svelte:head>


<NavBar />

{#if (recent.chapters.length != 0)}
    <Subtitle text="Recent" />
    <div class="chapters-container">
        {#each recent.chapters as chapter_data}
            <Chapter on:click={() => setRecentChapter(chapter_data)} {...chapter_data} />
        {/each}
    </div>
{/if}

<Subtitle text="All" />
<div class="chapters-container">
    {#each data.chapters as chapter_data}
        <Chapter on:click={() => setRecentChapter(chapter_data)} {...chapter_data} />
    {/each}
</div>
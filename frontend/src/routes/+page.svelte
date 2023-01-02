<script>
	import Chapter from "$lib/Chapter.svelte";
    import NavBar from "$lib/NavBar.svelte";
    import Subtitle from "$lib/Subtitle.svelte";
	import { onMount } from "svelte"; 
    import { getRecentChapters, setRecentChapter } from "$lib/recent.js"

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


<NavBar />

{#if (recent_chapters.length !== 0)}
    <Subtitle text="Recent" />
    <div class="chapters-container">
        {#each recent_chapters as chapter}
            <Chapter on:click={() => setRecentChapter(chapter)} {...chapter} />
        {/each}
    </div>
{/if}

<Subtitle text="All" />
<div class="chapters-container">
    {#each all_chapters as chapter}
        <Chapter on:click={() => setRecentChapter(chapter)} {...chapter} />
    {/each}
</div>
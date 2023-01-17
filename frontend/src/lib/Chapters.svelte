<script>
    import Subtitle from "$lib/Subtitle.svelte";
    import { setRecentChapter } from "$lib/recent.js"

    export let chapters;
    export let subtitle;
</script>

{#if (chapters.length !== 0)}
    <Subtitle text="{subtitle}" />
    <div class="chapters-container">
        {#each chapters as chapter}
            <a on:click={() => setRecentChapter(chapter)} href="/{chapter.number}">
                <div class="chapter-card">
                    <img src="/images/chapter{chapter.number}.webp" alt="{chapter.title} illustration">
                    <div class="chapter-texts-container">
                        <h3 class="small-text-bold chapter-small-text-bold">Chapter {chapter.number}</h3>
                        <p class="small-text chapter-small-text">{chapter.title}</p>
                    </div>
                </div> 
            </a>
        {/each}
    </div>
{/if}


<style>
.chapter-card {
    box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2);
    transition: box-shadow 0.3s;
    border-radius: 5px;
    width: 250px;
    margin: 10px;
}
@media screen and (max-width:375px) {
.chapter-card {
    width:95%;
}
}

.chapter-card>img {
    border-radius: 5px 5px 0 0;
    width: 100%;
    height: 150px;
}

.chapter-card:hover {
    box-shadow: 0 8px 16px 0 rgba(0, 0, 0, 0.2);
}

.chapter-texts-container {
    padding: 2px 0px;
}

.chapter-small-text-bold {
    margin: 5px;
}

.chapter-small-text {
    margin: 5px;
    margin-bottom: 10px;
}
</style>
<script>
    export let chapter = null;
    export let exercise = null;
</script>

<h2 class="subtitle-text">
    <a href="/">Chapters</a>
    {#if chapter}
        <span class="highlight-text"> > </span>
        <a href="/{chapter}">Chapter {chapter}</a>
    {/if}
    {#if exercise}
        <span class="highlight-text"> > </span>
        <a href="/{exercise}">Exercise {exercise}</a>
    {/if}
</h2>

<style>
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
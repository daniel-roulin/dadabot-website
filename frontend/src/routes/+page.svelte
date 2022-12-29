<script>
	import Chapter from "$lib/Chapter.svelte";
    import NavBar from "$lib/NavBar.svelte";

    export let data;
</script>

<svelte:head>
	<title>Dadabot</title>
	<meta name="description" content="Dadabot: Never do your physics homework again!" />
</svelte:head>

<NavBar />
<h2 class="subtitle-text">
    <a href="/">Recent</a>
</h2>
<div class="chapters-container">
    {#each data.chapters as chapter_data}
        <Chapter {...chapter_data} />
    {/each}
</div>

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
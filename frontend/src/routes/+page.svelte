<script>
	import Chapter from "./Chapter.svelte";
    import NavBar from "./NavBar.svelte";

    export let data;
</script>

<svelte:head>
	<title>Dadabot</title>
	<meta name="description" content="Dadabot: Never do your physics homework again!" />
</svelte:head>

<NavBar />
<div class="chapters-container">
    {#each data.chapters as chapter_data}
        <Chapter {...chapter_data} />
    {/each}
</div>
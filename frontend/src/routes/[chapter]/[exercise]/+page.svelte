<script>
    import NavBar from "$lib/NavBar.svelte";
    import PdfViewer from "$lib/PdfViewer.svelte";

    export let data

    $: pdf_path = `/api?chapter=${data.chapter}&exercise=${data.exercise}`
</script>

<svelte:head>
	<title>Exercise {data.exercise} Chapter {data.chapter}</title>
	<meta name="description" content="Exercise {data.exercise} of chapter {data.chapter}" />
</svelte:head>

<NavBar chapter={data.chapter} exercise={data.exercise} />

<PdfViewer pdf_path={pdf_path} />
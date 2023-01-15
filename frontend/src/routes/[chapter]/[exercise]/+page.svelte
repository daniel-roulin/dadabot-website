<script>
    import NavBar from "$lib/NavBar.svelte";
    import PdfViewer from "$lib/PdfViewer.svelte";

    export let data

    $: pdf_path = `/api?chapter=${data.chapter}&exercise=${data.exercise}`
</script>

<svelte:head>
	<title>Exercise {data.exercise} Chapter {data.chapter}</title>
    <meta property="og:title" content="Exercise {data.exercise} Chapter {data.chapter}">
    <meta name="twitter:title" content="Exercise {data.exercise} Chapter {data.chapter}">
    
	<meta name="description" content="Exercise {data.exercise} of chapter {data.chapter}" />
    <meta property="og:description" content="Exercise {data.exercise} of chapter {data.chapter}">
    <meta name="twitter:description" content="Exercise {data.exercise} of chapter {data.chapter}">
</svelte:head>

<PdfViewer pdf_path={pdf_path} />
<script>
    export let data

    import NavBar from "$lib/NavBar.svelte";
	import PdfViewer from "$lib/PdfViewer.svelte";

    $: pdf_path = `/api?chapter=${data.chapter_number}&exercise=${data.exercise_number}`
</script>

<svelte:head>
	<title>Exercise {data.exercise_number} Chapter {data.chapter_number}</title>
	<meta name="description" content="Exercise {data.exercise_number} of chapter {data.chapter_number}" />
</svelte:head>

<NavBar chapter={data.chapter_number} exercise={data.exercise_number} />

<PdfViewer pdf_path={pdf_path} />
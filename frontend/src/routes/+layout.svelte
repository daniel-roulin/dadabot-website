<script>
	import Header from '$lib/Header.svelte';
	import Footer from '$lib/Footer.svelte';
	import './styles.css';
</script>

<div class="app">
	<Header />

	<slot />

	<div style="height: 30px;"></div>
	<Footer/>
</div>
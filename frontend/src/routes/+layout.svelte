<script>
	import Header from './Header.svelte';
	import Footer from './Footer.svelte';
	import './styles.css';
</script>

<div class="app">
	<Header />

	<slot />

	<div style="height: 30px;"></div>
	<Footer/>
</div>
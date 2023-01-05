<script>
    export let search;
</script>

<header>
    <div class="header-items">
        <form action="#" class="search">
            <input bind:value={search} type="search" placeholder="Search..." name="">
            <button type="submit" class="button">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 40 40" >
                    <path fill=#BDBDBD stroke=#BDBDBD d="M39.8 41.95 26.65 28.8q-1.5 1.3-3.5 2.025-2 .725-4.25.725-5.4 0-9.15-3.75T6 18.75q0-5.3 3.75-9.05 3.75-3.75 9.1-3.75 5.3 0 9.025 3.75 3.725 3.75 3.725 9.05 0 2.15-.7 4.15-.7 2-2.1 3.75L42 39.75Zm-20.95-13.4q4.05 0 6.9-2.875Q28.6 22.8 28.6 18.75t-2.85-6.925Q22.9 8.95 18.85 8.95q-4.1 0-6.975 2.875T9 18.75q0 4.05 2.875 6.925t6.975 2.875Z" />
                </svg>
            </button>
        </form>
        <a href="/">
            <img class="logo" alt="Dadabot logo" src="/images/logo.png">
        </a>        
    </div>
    <hr class="divider">
</header>

<style>
header {
    margin: 0;
    padding-top: 10px;
    top: 0px;
    position: sticky;
    background-color: var(--background1);
}

.header-items {
    width: 100%;
    display: flex;
    align-items: center;
}

.logo {
    height: 35px;
    margin-left: 15px;
    margin-right: 5px;
}

.divider {
    border: 1px solid var(--secondary2);
}

.search {
    width: 100%;
    height: 35px;
    margin-left: 15px;
    margin-right: 0px;
    border-radius: 50px;
    border: 1px var(--secondary2) solid;
    background-color: var(--background2);

    display: flex;
    align-items: center;
}

.search input[type=search] {
    height: 25px;
    width: 80%;

    font-size: 15px;

    background: none;
    border: none;
    border-color: transparent;
    outline: none;
    color: var(--main);

    padding: 15px;

    flex: 1 1 100px
}

.search,
input::placeholder {
    color: var(--secondary2);
}

.button {
    height: 20px;
    width: 20px;
    padding: 0px;
    margin-right: 10px;
    background: none;
    border: none;
    border-color: transparent;
    flex: 0 1 20px;
}
</style>
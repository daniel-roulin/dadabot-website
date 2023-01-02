<script>
    export let chapter;
    export let number;
    export let content;
</script>

<a on:click href="{chapter}/{number}">
    <div class="exercise-container">
        <h4 class="small-text-bold exercise-small-text-bold">Exercise {number}</h4>
        <p class="small-text exercise-small-text">{content}</p>
    </div>
</a>

<style>
.exercise-container {
    display: flex;
    align-items: center;
}

.exercise-small-text-bold {
    white-space: nowrap;
    margin: 10px;
}

.exercise-small-text {
    flex-grow: 1;
    text-overflow: ellipsis;
    white-space: nowrap;
    overflow: hidden;
    margin-right: 10px;
}
</style>
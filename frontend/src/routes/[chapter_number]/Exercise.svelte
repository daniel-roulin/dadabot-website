<script>
    export let chapter_number;
    export let exercise_number;
    export let exercise_summary;
</script>

<a href="{chapter_number}/{exercise_number}">
    <div class="exercise-container">
        <h4 class="small-text-bold exercise-small-text-bold">Exercise {exercise_number}</h4>
        <p class="small-text exercise-small-text">{exercise_summary}</p>
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
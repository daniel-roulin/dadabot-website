<script>
    import Subtitle from "$lib/Subtitle.svelte"
    import { setRecentExercise } from "$lib/recent.js"

    export let exercises;
    export let subtitle;
    export let search = null;

    function snippet(content, search) {
        const startMarker = "<span class=\"highlight-text\">"
        const endMarker = "</span>"
        const pattern = new RegExp(search, "i")
        let finalString = "";
        while (true) {
            let match = content.search(pattern);
            if (match == -1) {
                break;
            }
            let start = 0
            if (finalString.length == 0 && match > 20) {
                start = content.indexOf(" ", match - 20) + 1;
                finalString = "...";
            }
            finalString += content.slice(start, match)
                        + startMarker
                        + content.slice(match, match + search.length)
                        + endMarker
            content = content.slice(match + search.length)
        }
        return finalString + content;
    }
</script>

{#if (exercises.length !== 0)}
    <Subtitle text="{subtitle}" />
    {#each exercises as exercise, index}
        <a on:click on:click={() => setRecentExercise(exercise.chapter, exercise)} href="/{exercise.chapter}/{exercise.number}">
            <div class="exercise-container">
                {#if search}
                    <h4 class="small-text-bold exercise-small-text-bold">Ch. {exercise.chapter} Ex. {exercise.number}</h4>
                    <p class="small-text exercise-small-text">{@html snippet(exercise.content, search)}</p>
                {:else}
                    <h4 class="small-text-bold exercise-small-text-bold">Exercise {exercise.number}</h4>
                    <p class="small-text exercise-small-text">{exercise.content}</p>
                {/if}
            </div>
        </a>
        {#if !(index === exercises.length-1)}
            <hr class="exercise-divider">
        {/if}
    {/each}
{/if}

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

.exercise-divider {
    margin: 0px 10px;
    border: 1px solid var(--secondary2);
}
</style>
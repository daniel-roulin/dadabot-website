import {error, json} from '@sveltejs/kit';
import db from "$lib/db.js";

export function GET({url}) {
    const query = url.searchParams.get("q");
    if (!query) throw error(400, "parameter query (q) is a required field that is missing.");
    
    const results = search(query);

    return json(results)
}

function search(input) {
    // First, try to match the input string to a chapter and exercise pattern
    // For example, "45 35" should match
    const chapterExercisePattern = /^(\d+) (\d+)$/;
    const chapterExerciseMatch = input.match(chapterExercisePattern);
    if (chapterExerciseMatch) { // Return the specified exercise in the specified chapter
        const chapter = chapterExerciseMatch[1];
        const exercise = chapterExerciseMatch[2];
        return getExercise(chapter, exercise);
    }

    // Next, try to match the input string to a chapter and search query pattern
    // For example, "45 electric" should match
    const chapterSearchPattern = /^(\d+) (.*)$/;
    const chapterSearchMatch = input.match(chapterSearchPattern);
    if (chapterSearchMatch) { // Return all exercises in the specified chapter containing the search query
        const chapter = chapterSearchMatch[1];
        const query = chapterSearchMatch[2];
        return searchExercisesInChapter(chapter, query);
    }

    // Next, try to match the input string to a chapter pattern
    // For example, "45" should match
    const chapterPattern = /^\d+$/;
    const chapterMatch = input.match(chapterPattern);
    if (chapterMatch) { // Return all exercises in the specified chapter
        const chapter = chapterMatch[0];
        return getExercisesInChapter(chapter);
    }

    // Finally, assume that the input is a search query
    // Return all exercises that contain the search query
    return searchExercises(input);
}

function getExercise(chapter, exercise) {
    const stmt = db.prepare(`
    SELECT chapter, number, content
    FROM exercises
    WHERE chapter = ? AND number = ?
    ;`);
    return stmt.all(chapter, exercise);
}

function getExercisesInChapter(chapter) {
    const stmt = db.prepare(`
    SELECT chapter, number, content
    FROM exercises
    WHERE chapter = ?
    ;`);
    return stmt.all(chapter);    
}

function searchExercises(query) {
    const stmt = db.prepare(`
    SELECT chapter, number, exercises_fts.content AS content
    FROM exercises INNER JOIN exercises_fts ON exercises.id = exercises_fts.rowid
    WHERE exercises_fts MATCH ?
    ORDER BY rank LIMIT 100
    ;`);
    return stmt.all(query + "*");
}

function searchExercisesInChapter(chapter, query) {
    const stmt = db.prepare(`
    SELECT chapter, number, exercises_fts.content AS content
    FROM exercises INNER JOIN exercises_fts ON exercises.id = exercises_fts.rowid
    WHERE chapter = ? AND exercises_fts MATCH ?
    ORDER BY rank LIMIT 100
    ;`);
    return stmt.all(chapter, query + "*");
}
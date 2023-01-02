import { error } from '@sveltejs/kit';
import db from "$lib/db.js";

export function load({ params }) {
    const stmt = db.prepare('SELECT number, content FROM exercises WHERE chapter = ? AND number = ?;');
    const row = stmt.get(params.chapter, params.exercise);

    if (!row) throw error(404);

    return {
        chapter: params.chapter,
        exercise: params.exercise,
    };
}
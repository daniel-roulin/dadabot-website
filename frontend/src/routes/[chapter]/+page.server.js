import { error } from '@sveltejs/kit';
import db from "$lib/db.js";

export function load({ params }) {
    const stmt = db.prepare('SELECT chapter, number, content FROM exercises WHERE chapter = ?;');
    const rows = stmt.all(params.chapter);

    if (rows.length === 0) throw error(404);

    return {chapter:params.chapter, exercises: rows}
}
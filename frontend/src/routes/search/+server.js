import { error, json } from '@sveltejs/kit';
import db from "$lib/db.js";

export function GET({ url }) {
    const query = url.searchParams.get("q");
    if (!query) throw error(400, "parameter query (q) is a required field that is missing.");

    const stmt = db.prepare(`
    SELECT chapter, number, snippet(exercises_fts, 0, '<b>', '</b>', '...', 20) AS content
    FROM exercises INNER JOIN exercises_fts ON exercises.id = exercises_fts.rowid
    WHERE exercises_fts MATCH ?
    ORDER BY rank LIMIT 100;
    `);
    const rows = stmt.all(query + "*");

    return json(rows)
}
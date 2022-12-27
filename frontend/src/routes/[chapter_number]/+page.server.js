import { error } from '@sveltejs/kit';
import Database from 'better-sqlite3';

export function load({ params }) {
    const db = new Database('./database/database.db');
    db.pragma('journal_mode = WAL');

    const stmt = db.prepare('SELECT number, content FROM exercises WHERE chapter_id = ?;');
    const rows = stmt.all(params.chapter_number);

    if (!rows) throw error(404);

    db.close();

    return {
        chapter_number: params.chapter_number,
        exercises: rows.map((row) => ({
            chapter_number: params.chapter_number,
            exercise_number: row.number,
            exercise_summary: row.content.substring(0, 300),
        }))
    };
}
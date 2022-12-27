import { error } from '@sveltejs/kit';
import Database from 'better-sqlite3';

export function load({ params }) {
    const db = new Database('./database/database.db');
    db.pragma('journal_mode = WAL');

    const stmt = db.prepare('SELECT number, content FROM exercises WHERE chapter_id = ? AND number = ?;');
    const row = stmt.get(params.chapter_number, params.exercise_number);

    if (!row) throw error(404);

    db.close();

    return {
        chapter_number: params.chapter_number,
        exercise_number: params.exercise_number,
    };
}
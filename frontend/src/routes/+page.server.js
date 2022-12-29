import Database from 'better-sqlite3';

export function load() {
    const db = new Database('./database/database.db');
    db.pragma('journal_mode = WAL');

    const stmt = db.prepare('SELECT number, title, image_path FROM chapters ORDER BY number');
    const rows = stmt.all();

    db.close();

    return {
        chapters: rows.map((row) => ({
            chapter_number: row.number,
            chapter_title: row.title,
            image_url: row.image_path
        }))
    };
}

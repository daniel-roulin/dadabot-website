import db from "$lib/db.js"

export function load() {
    const stmt = db.prepare('SELECT number, title, image_path FROM chapters ORDER BY number');
    const rows = stmt.all();

    return {chapters: rows}
}

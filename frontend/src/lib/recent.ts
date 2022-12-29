export function getRecentChapters() {
    var recent = localStorage.getItem("recentChapters");
    if (recent) {
        return JSON.parse(recent);
    } else {
        return [];
    }
}

export function setRecentChapter(chapter_data) {
    let recent = getRecentChapters();
    for (var i = 0; i < recent.length; i++) {
        if (recent[i].chapter_number == chapter_data.chapter_number) {
            recent.splice(i, 1);
            break;
        };
    };
    recent.unshift(chapter_data);
    if (recent.length > 5) {
        recent.pop();
    }
    localStorage.setItem("recentChapters", JSON.stringify(recent));
}

export function getRecentExercises() {
    var recent = localStorage.getItem("recentExercises");
    if (recent) {
        return JSON.parse(recent);
    } else {
        return [];
    }
}

export function setRecentExercise(exercise_data) {
    let recent = getRecentExercises();
    for (var i = 0; i < recent.length; i++) {
        if (recent[i].exercise_number == exercise_data.exercise_number) {
            recent.splice(i, 1);
            break;
        };
    };
    recent.unshift(exercise_data);
    if (recent.length > 10) {
        recent.pop();
    }
    localStorage.setItem("recentExercises", JSON.stringify(recent));
}
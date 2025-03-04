async function uploadNote() {
    const title = document.getElementById("title").value;
    const content = document.getElementById("content").value;

    const response = await fetch("/upload", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ title, content })
    });

    const data = await response.json();
    alert(data.message);
    fetchNotes();
}

async function fetchNotes() {
    const response = await fetch("/notes");
    const notes = await response.json();
    const notesList = document.getElementById("notesList");
    notesList.innerHTML = "";
    notes.forEach(note => {
        const li = document.createElement("li");
        li.innerHTML = `<a href="#" onclick="viewNote('${note.id}')">${note.name}</a>`;
        notesList.appendChild(li);
    });
}

async function viewNote(fileId) {
    const response = await fetch(`/note/${fileId}`);
    const data = await response.json();
    alert("Content: " + data.content);
}

fetchNotes();

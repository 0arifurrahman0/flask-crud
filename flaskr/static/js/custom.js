function deleteNote(note_id) {
    fetch('/note-delete', {
        method: 'POST',
        body: JSON.stringify({note_id: note_id})
    }).then((res) => {
        window.location.href = '/home';
    });
}
function set_editor(note_id) {
    fetch(`/get_note/${note_id}`, {
        method: 'POST'
      })
      .then(response => response.json())
      .then(result => {
        document.querySelector('#editor').value = result[0].content;
      })
}


function set_selected(type, id) {
    document.querySelector('#selected_entry').dataset.type = type;
    document.querySelector('#selected_entry').innerHTML = id;
}


function load_notes(tag_id=0) {
    document.querySelector('#entry_list').innerHTML = '';

    fetch('/get_notes', {
        method: 'POST'
      })
      .then(response => response.json())
      .then(result => {
        result.forEach(element => {
            if (tag_id != 0) {
                // validate if this note has the right tag id
                found = false;
                for (i=0; i < element.tags.length; ++i) {
                    if (tag_id == element.tags[i]) {
                        found = true;
                    }
                }
                
                if (!found) {
                    return; // https://stackoverflow.com/a/48802390
                }
            }
            note = document.createElement('div');
            note.className = 'note-entry';
            note.dataset.id = element.id;
            note.innerHTML = element.content[0];
            document.querySelector('#entry_list').append(note);
        });
      })
      .then(() => {
        document.querySelectorAll('.note-entry').forEach(element => {
            element.addEventListener('click', note => {
                set_selected('note', note.target.dataset.id);
                set_editor(note.target.dataset.id);
            })
        })
      })
}


function load_tags() {
    document.querySelector('#entry_list').innerHTML = '';

    fetch('/get_tags', {
        method: 'POST'
      })
      .then(response => response.json())
      .then(result => {
        result.forEach(element => {
            tag = document.createElement('div');
            tag.className = 'tag-entry';
            tag.dataset.id = element.id;
            tag.innerHTML = element.name;
            document.querySelector('#entry_list').append(tag);
        });
      })
      .then(() => {
        document.querySelectorAll('.tag-entry').forEach(element => {
            element.addEventListener('click', tag => {
                set_selected('tag', tag.target.dataset.id);
                load_notes(tag_id=tag.target.dataset.id);
                document.querySelector('#page_title').innerHTML = `#${tag.target.innerHTML}`;
            })
        })
      })    
}

document.addEventListener('DOMContentLoaded', () => {
    document.querySelector('#all_notes').addEventListener('click', () => {
        load_notes();
        set_selected('none', 0);
        document.querySelector('#page_title').innerHTML = 'All Notes';
        document.querySelector('#editor').value = '';
    })

    document.querySelector('#all_tags').addEventListener('click', () => {
        load_tags();
        set_selected('none', 0);
        document.querySelector('#page_title').innerHTML = 'All Tags';
        document.querySelector('#editor').value = '';
    })

    // All notes by default
    document.getElementById('all_notes').click();
})
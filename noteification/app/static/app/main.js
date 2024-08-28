function set_editor(note_id) {
    fetch(`/get_note/${note_id}`, {
        method: 'POST'
      })
      .then(response => response.json())
      .then(result => {
        document.querySelector('#editor').value = result[0].content;
      })
      .then(() => {
        set_selected('note', note_id);
        })
}


function set_selected(type, id) {
    document.querySelector('#selected_entry').dataset.type = type;
    document.querySelector('#selected_entry').innerHTML = id;
}


function add_new_note() {
    document.querySelector('#page_title').innerHTML = 'All Notes';
    const add_button = document.createElement('button');
    add_button.id = 'add_note';
    add_button.innerHTML = '+';
    document.querySelector('#page_title').append(add_button);

    add_button.addEventListener('click', () => {
        fetch('/create_note', {
            method: 'POST',
            body: JSON.stringify({
                content: "" 
            })
        })
        .then(response => response.json())
        .then(result => {
            location.reload(); // FIXME clunky UI must select the new No Title note
        })
    })
}


function add_new_tag() {
    document.querySelector('#page_title').innerHTML = 'All Tags';
    const add_button = document.createElement('button');
    add_button.id = 'add_tag';
    add_button.innerHTML = '+';
    document.querySelector('#page_title').append(add_button);

    add_button.onclick = () => {
        document.querySelector("#tag_adder").style.display = 'block';
        document.querySelector("#tag_adder_submit").onclick = () => {
            fetch('create_tag', {
                method: 'POST',
                body: JSON.stringify({
                    name: document.querySelector('#small_input').value
                }) 
            })
            .then(() => {
                document.querySelector('#small_input').value = '';
                document.querySelector("#tag_adder").style.display = 'none';
                load_tags();
            })
        }
    }
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
            const first_line = element.content.substring(0, element.content.indexOf('\n'));
            if (first_line === '') {
                note.innerHTML = 'No Title';
            }
            else {
                note.innerHTML = first_line;
            }
            document.querySelector('#entry_list').append(note);
        });
      })
      .then(() => {
        document.querySelectorAll('.note-entry').forEach(element => {
            element.addEventListener('click', note => {
                set_selected('none', note.target.dataset.id); // to avoid copying from last note
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
            container = document.createElement('div');

            tag = document.createElement('span');
            tag.className = 'tag-entry-text';
            tag.dataset.id = element.id;
            tag.innerHTML = element.name;
            container.append(tag);

            notes_button = document.createElement('button');
            notes_button.innerHTML = 'Notes';
            notes_button.className = 'tag-entry-notes';
            container.append(notes_button);
            
            document.querySelector('#entry_list').append(container);
        });
      })
      .then(() => {
        document.querySelectorAll('.tag-entry-text').forEach(element => {
            element.addEventListener('click', tag => {
                set_selected('tag', tag.target.dataset.id);
                load_notes(tag_id=tag.target.dataset.id);
                document.querySelector('#page_title').innerHTML = `#${tag.target.innerHTML}`;

                const rename = document.createElement('button');
                rename.id = 'rename_tag';
                rename.innerHTML = 'Rename';
                document.querySelector('#page_title').append(rename);
            })
        })

        // TODO add tag-entry-notes handler here
      })    
}

document.addEventListener('DOMContentLoaded', () => {
    // show notes
    document.querySelector('#all_notes').addEventListener('click', () => {
        load_notes();
        set_selected('none', 0);
        document.querySelector('#editor').value = '';
        add_new_note();
    })

    // show tags
    document.querySelector('#all_tags').addEventListener('click', () => {
        load_tags();
        set_selected('none', 0);
        document.querySelector('#editor').value = '';
        add_new_tag();
    })

    // update note as it is edited
    document.querySelector('#editor').addEventListener('input', () => {
        // we must be selecting a note
        if (document.querySelector('#selected_entry').dataset.type === 'note') {
            fetch(`/update_note/${document.querySelector('#selected_entry').innerHTML}`, {
                method: 'POST',
                body: JSON.stringify({
                    content: document.querySelector('#editor').value
                }) 
            })
            .then(() => {
                // update the text preview in #entry_list
                const id = document.querySelector('#selected_entry').innerHTML.toString();
                const editor = document.querySelector('#editor').value;
                const first_line = editor.substring(0, editor.indexOf('\n'));
                console.log(first_line);
                if (first_line === '') {
                    document.querySelector(`[data-id="${id}"]`).innerHTML = 'No Title';
                }
                else {
                    document.querySelector(`[data-id="${id}"]`).innerHTML = first_line;
                }
            })
        }
    })

    // 'All Notes' by default
    document.getElementById('all_notes').click();
})
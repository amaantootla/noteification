document.addEventListener('DOMContentLoaded', () => {

    const notes_tab = document.getElementById('notes-tab');
    const folders_tab = document.getElementById('folders-tab');
    const notes_content = document.getElementById('notes-content');
    const folders_content = document.getElementById('folders-content');

    // toggle
    notes_tab.addEventListener('click', () => {
        notes_tab.classList.remove('btn-secondary');
        notes_tab.classList.add('btn-success');

        if (folders_tab.classList.contains('btn-success')) {
            folders_tab.classList.remove('btn-success');
            folders_tab.classList.add('btn-secondary');
        }

        notes_content.classList.remove('hidden');
        folders_content.classList.add('hidden');

        notes_tab.classList.add('active');
        folders_tab.classList.remove('active');

        notes_content.classList.remove('hidden');
        folders_tab.classList.add('hidden');
    })
    
    // toggle
    folders_tab.addEventListener('click', () => {
        folders_tab.classList.remove('btn-secondary');
        folders_tab.classList.add('btn-success');

        if (notes_tab.classList.contains('btn-success')) {
            notes_tab.classList.remove('btn-success');
            notes_tab.classList.add('btn-secondary');
        }

        folders_content.classList.remove('hidden');
        notes_content.classList.add('hidden');

        folders_tab.classList.add('active');
        notes_tab.classList.remove('active');

        folders_content.classList.remove('hidden');
        notes_content.classList.add('hidden');
    })

    // default view
    notes_tab.click();
})
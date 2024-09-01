document.addEventListener('DOMContentLoaded', () => {

    const notes_tab = document.getElementById('notes-tab');
    const audio_tab = document.getElementById('audio-tab');
    const notes_content = document.getElementById('notes-content');
    const audio_content = document.getElementById('audio-content');

    // toggle
    notes_tab.addEventListener('click', () => {
        notes_tab.classList.remove('btn-secondary');
        notes_tab.classList.add('btn-success');

        if (audio_tab.classList.contains('btn-success')) {
            audio_tab.classList.remove('btn-success');
            audio_tab.classList.add('btn-secondary');
        }

        notes_content.classList.remove('hidden');
        audio_content.classList.add('hidden');

        notes_tab.classList.add('active');
        audio_tab.classList.remove('active');

        notes_content.classList.remove('hidden');
        audio_tab.classList.add('hidden');
    })
    
    // toggle
    audio_tab.addEventListener('click', () => {
        audio_tab.classList.remove('btn-secondary');
        audio_tab.classList.add('btn-success');

        if (notes_tab.classList.contains('btn-success')) {
            notes_tab.classList.remove('btn-success');
            notes_tab.classList.add('btn-secondary');
        }

        audio_content.classList.remove('hidden');
        notes_content.classList.add('hidden');

        audio_tab.classList.add('active');
        notes_tab.classList.remove('active');

        audio_content.classList.remove('hidden');
        notes_content.classList.add('hidden');
    })

    document.querySelector('#new_note').onclick = () => {
        window.location.href = 'createdit_note/0/index';
    }

    // default view
    notes_tab.click();
})
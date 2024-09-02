document.addEventListener('DOMContentLoaded', () => {

    const notes_tab = document.getElementById('notes-tab');
    const bonus_tab = document.getElementById('bonus-tab');
    const notes_content = document.getElementById('notes-content');
    const bonus_content = document.getElementById('bonus-content');

    // toggle
    notes_tab.addEventListener('click', () => {
        notes_tab.classList.remove('btn-secondary');
        notes_tab.classList.add('btn-success');

        if (bonus_tab.classList.contains('btn-success')) {
            bonus_tab.classList.remove('btn-success');
            bonus_tab.classList.add('btn-secondary');
        }

        notes_content.classList.remove('hidden');
        bonus_content.classList.add('hidden');

        notes_tab.classList.add('active');
        bonus_tab.classList.remove('active');

        notes_content.classList.remove('hidden');
        bonus_tab.classList.add('hidden');

        bonus_content.style.display = 'none';
    })
    
    // toggle
    bonus_tab.addEventListener('click', () => {
        bonus_content.style.display = 'flex';

        bonus_tab.classList.remove('btn-secondary');
        bonus_tab.classList.add('btn-success');

        if (notes_tab.classList.contains('btn-success')) {
            notes_tab.classList.remove('btn-success');
            notes_tab.classList.add('btn-secondary');
        }

        bonus_content.classList.remove('hidden');
        notes_content.classList.add('hidden');

        bonus_tab.classList.add('active');
        notes_tab.classList.remove('active');

        bonus_content.classList.remove('hidden');
        notes_content.classList.add('hidden');

        fetch('https://uselessfacts.jsph.pl/api/v2/facts/random', {
            method: 'GET'
        })
        .then(response => response.json())
        .then(result => {
            bonus_content.querySelector('#fact').innerHTML = result["text"];
        })
    })

    document.querySelector('#new_note').onclick = () => {
        window.location.href = 'createdit_note/0/index';
    }

    // default view
    notes_tab.click();
})
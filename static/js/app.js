document.addEventListener('DOMContentLoaded', () => {
    const board = document.getElementById('board');
    if (!board || !window.levelData) return;

    const level = window.levelData;
    const graph = level.graph;
    const nodeNames = Object.keys(graph);
    const positions = {};
    const selected = [];

    const layout = {
        A: { x: 80, y: 220 },
        B: { x: 220, y: 140 },
        C: { x: 220, y: 300 },
        D: { x: 360, y: 140 },
        E: { x: 360, y: 300 },
        F: { x: 520, y: 220 },
        G: { x: 520, y: 220 },
        H: { x: 520, y: 220 },
        I: { x: 520, y: 220 },
        J: { x: 520, y: 220 },
        K: { x: 520, y: 220 },
        L: { x: 520, y: 220 },
        M: { x: 520, y: 220 },
        N: { x: 520, y: 220 },
        O: { x: 520, y: 220 },
        P: { x: 520, y: 220 },
        Q: { x: 520, y: 220 },
        R: { x: 520, y: 220 },
        S: { x: 520, y: 220 },
        T: { x: 520, y: 220 }
    };

    const letters = Object.keys(level.graph);
    const renderNode = (name, index) => {
        const pos = layout[name] || {
            x: 120 + (index % 4) * 120,
            y: 120 + Math.floor(index / 4) * 130
        };
        positions[name] = pos;

        const node = document.createElement('button');
        node.className = 'node';
        if (name === level.goal) node.classList.add('goal');
        node.type = 'button';
        node.dataset.name = name;
        node.textContent = name;
        node.style.left = `${pos.x}px`;
        node.style.top = `${pos.y}px`;
        node.addEventListener('click', () => {
            if (!selected.includes(name)) {
                selected.push(name);
                node.classList.add('selected');
                updateSelectedDisplay();
            }
        });
        board.appendChild(node);
    };

    letters.forEach(renderNode);

    const pathDisplay = document.getElementById('selected-path');
    const status = document.getElementById('status');
    const clearButton = document.getElementById('reset-path');
    const validateButton = document.getElementById('validate-path');

    function updateSelectedDisplay() {
        pathDisplay.textContent = selected.length ? selected.join(' → ') : 'Aucun neurone sélectionné';
    }

    clearButton.addEventListener('click', () => {
        selected.length = 0;
        document.querySelectorAll('.node.selected').forEach(node => node.classList.remove('selected'));
        updateSelectedDisplay();
        status.textContent = 'Le chemin a été réinitialisé.';
    });

    validateButton.addEventListener('click', async () => {
        if (!selected.length) {
            status.textContent = 'Choisis au moins un neurone avant de valider.';
            return;
        }

        const response = await fetch('/api/validate', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ level_id: level.id, selection: selected })
        });
        const result = await response.json();
        status.textContent = result.message || 'Validation en cours...';

        if (result.ok) {
            const stars = result.score.stars;
            const xp = result.score.xp;
            document.getElementById('reward').textContent = `Récompense : ${stars} étoile(s) • ${xp} XP`;
            const dialogue = document.getElementById('aria-dialogue');
            dialogue.textContent = `ARIA : Mission réussie. Tu as restauré le réseau avec ${stars} étoiles et ${xp} XP.`;
        } else if (result.hint) {
            const hints = document.getElementById('aria-dialogue');
            hints.textContent = `ARIA : ${result.hint}`;
        }
    });

    updateSelectedDisplay();
});

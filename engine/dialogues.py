def get_dialogue_lines(level_id):
    dialogues = {
        1: [
            "ARIA : Nous avons enfin accès au premier réseau. Observe les neurones et les connexions.",
            "NEO : Je peux entendre des impulsions très faibles.",
            "ARIA : Relie les neurones du départ à la cible sans casser la logique du réseau."
        ],
        2: [
            "ARIA : Le secteur des synapses est actif. Ici, plusieurs chemins existent, mais un seul est fiable.",
            "NEO : Pourquoi certaines connexions cessent-elles de fonctionner ?",
            "ARIA : Parce que des liaisons sont invalides. Le bon chemin suit la logique du graphe."
        ],
        3: [
            "ARIA : Les mémoires du réseau sont stockées sous forme de séquences. Chaque neurone conserve une trace.",
            "NEO : J'entends un motif récurrent.",
            "ARIA : Oui. Le chemin correct reprend la structure logique du souvenir."
        ],
        4: [
            "ARIA : Un signal parasite déforme la transmission. Nous devons filtrer les liaisons bruitées.",
            "NEO : Alors il faut trier les bonnes voies de l'énigme.",
            "ARIA : Exactement. Tout le réseau doit être remis en ordre."
        ],
        5: [
            "ARIA : Nous entrons dans un grand réseau profond. Les chemins se multiplient.",
            "NEO : L'univers ressemble à un immense graphe.",
            "ARIA : C'est bien cela : chaque connexion représente un état possible."
        ],
        6: [
            "ARIA : Une perturbation se déclare. Certaines relations sont incohérentes.",
            "NEO : Comment distinguer les anomalies ?",
            "ARIA : En comparant le réseau et en testant chaque chemin, comme dans un algorithme."
        ],
        7: [
            "ARIA : Nous approchons de la source du dysfonctionnement.",
            "NEO : Le réseau ne semble plus stable.",
            "ARIA : Il faut réunir toutes les leçons apprises pour retrouver l'origine."
        ],
        8: [
            "ARIA : Dernière phase. Le système a besoin d'une reconstruction totale.",
            "NEO : Je peux enfin voir le cœur du problème.",
            "ARIA : Bien. L'unité neuronale doit être restaurée, pierre après pierre."
        ],
    }
    return dialogues.get(level_id, ["ARIA : Le réseau ne répond pas encore."])

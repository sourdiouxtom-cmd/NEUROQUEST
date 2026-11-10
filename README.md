# NEUROQUEST

NEUROQUEST est un projet de jeu d'aventure scientifique développé en Python avec Flask comme interface navigateur.

Le principe : le joueur explore un univers futuriste inspiré des réseaux neuronaux, résout des énigmes sur les graphes et découvre le fonctionnement des synapses à travers une narration scientifique simplifiée.

## Objectif

- Rendre visible les concepts NSI : graphes, chemins, BFS, DFS, dictionnaires, listes, récursivité.
- Créer un prototype jouable avec plusieurs niveaux.
- démontrer un projet sérieux devant un jury.

## Structure du projet

- app.py : point d'entrée Flask
- engine/ : moteur du jeu, niveaux, progression, scores
- algorithms/ : graphes et algorithmes de recherche
- database/ : SQLite et sauvegardes
- levels/ : fichiers JSON des niveaux
- static/ : CSS et JavaScript
- templates/ : pages HTML
- tests/ : tests de validation

## Lancer le projet

1. Installer les dépendances :
   python -m pip install -r requirements.txt

2. Démarrer l'application :
   python app.py

3. Ouvrir le navigateur :
   http://localhost:5000/

## Règles de conception

- Le cœur du jeu reste en Python.
- Le navigateur sert uniquement à l'interface et aux interactions.
- Les algorithmes de graphe sont vraiment utilisés pour valider les niveaux.

## Auteurs

Projet de démonstration NEUROQUEST.

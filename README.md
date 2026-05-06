# BiblioCampus


Application Python de gestion de bibliothèque universitaire.

## Description

BiblioCampus permet de gérer simplement une bibliothèque universitaire :
ajouter des livres, les emprunter, les rendre et consulter des statistiques.
Toutes les données sont sauvegardées automatiquement dans un fichier JSON.

## Fonctionnalités

- Ajouter un livre
- Lister tous les livres
- Rechercher un livre par titre ou auteur
- Emprunter un livre
- Rendre un livre
- Afficher des statistiques (total, disponibles, empruntés)

## Structure du projet

biblio_campus/
├── main.py          # Point d'entrée
├── menu.py          # Menu principal et navigation
├── books.py         # Gestion des livres
├── loans.py         # Gestion des emprunts
├── stats.py         # Statistiques
├── storage.py       # Lecture/écriture JSON
├── data/
│   └── library.json # Données persistantes
├── tests/
│   └── test_basic.py
├── README.md
├── .gitignore
└── requirements.txt

## Installation

git clone <URL_DU_DEPOT>
cd biblio_campus
python main.py

## Utilisation

Lancez l'application et suivez le menu interactif :

========== BiblioCampus ==========
1. Ajouter un livre
2. Lister les livres
3. Rechercher un livre
4. Emprunter un livre
5. Rendre un livre
6. Voir les statistiques
0. Quitter
==================================

## Équipe

Collaborateur A — Structure, menu principal, storage
Collaborateur B — Gestion des livres
Collaborateur C — Emprunts, retours, statistiques

## Licence

Projet académique — usage éducatif uniquement.
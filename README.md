# Pong Game – Python / Pygame

## Description

Une version moderne du jeu classique **Pong** pour deux joueurs sur le même ordinateur. Le jeu propose une balle dynamique, des effets visuels et un écran de démarrage interactif.

## Comment jouer

- **Joueur 1** : utiliser les touches **Z** (haut) et **S** (bas) pour déplacer la raquette.
- **Joueur 2** : utiliser les **flèches Haut/Bas** pour déplacer la raquette.

- La balle rebondit automatiquement sur les murs et les raquettes.

- **Objectif** : marquer le plus de points possible en faisant passer la balle derrière la raquette de l’adversaire.

- L’écran affiche le score des deux joueurs en haut de l’écran.

## Installation

1. Installer Python 3.8+
2. Installer Pygame :
    ```python
    pip install pygame
    ```
3. Cloner le dépôt :
    ```sh
    git clone https://github.com/Danyaal-Akhtar/Pong-game.git
    ````
4. Lancer le jeu :
    ```python
    python main.py
    ````
## Fonctionnalités

- Traînée visuelle derrière la balle (“effet en feu”).
- Changement de couleur de la balle à chaque rebond.
- Écran de démarrage interactif avec bouton **Start**.
- Déplacement fluide des raquettes, limité à l’écran.
- Score en temps réel pour suivre la partie.

## Organisation

- `main.py` – boucle principale et rendu
- `player.py` – mouvements des raquettes
- `ball.py` – logique de la balle et collisions
- `game.py` – gestion du score
- `effects.py` – traînée et effets visuels
- `colors.py` – gestion des couleurs de la balle
- `start.py` – écran de démarrage


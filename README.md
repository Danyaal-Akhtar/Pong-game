# Pong Game – Python / Pygame

## Description

Une version revisitée du jeu classique **Pong**, développée en **Python** avec **Pygame**. Deux joueurs peuvent s’affronter sur le même ordinateur avec des touches distinctes.

Le jeu inclut :

- Balle dynamique qui change de couleur à chaque rebond.
    
- Traînée derrière la balle pour un effet “en feu”.
    
- Écran de démarrage interactif avec bouton **Start**.
    
- Affichage du score en temps réel.
    
- Structure de code modulaire et facile à comprendre.
    

## Installation

1. Installer Python 3.8+
    
2. Installer Pygame :
    
    `pip install pygame`
    
3. Cloner le dépôt :
    
    `git clone <lien_du_dépôt>`
    
4. Lancer le jeu :
    
    `python main.py`
    

## Organisation

- `main.py` – boucle principale et rendu
    
- `player.py` – mouvements des raquettes
    
- `ball.py` – logique de la balle et collisions
    
- `game.py` – gestion du score
    
- `effects.py` – traînée et effets visuels
    
- `colors.py` – gestion des couleurs de la balle
    
- `start.py` – écran de démarrage

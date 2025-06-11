import pygame
from pygame.locals import *


# Initialisation du jeu
def init_game():
    pygame.init()
    window_resolution = (840, 600)  # Largeur et Hauteur
    window_surface = pygame.display.set_mode(window_resolution)  # Résolution de la fenêtre
    pygame.display.set_caption("Jeu de Pong")  # Titre de la fenêtre
    return window_surface,window_resolution



# Gestion des événements
def events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Lorsque l'on quitte la fenêtre avec une croix
            return False
    return True

# Mouvement du joueur 1
def player1(position_y_joueur1, height_joueur1, window_resolution):
    keys = pygame.key.get_pressed()
    speed = 0.6  # Vitesse d'exécution

    if keys[pygame.K_z] and position_y_joueur1 > 0:  # Eviter que le rectangle ne dépasse pas le haut de l'écran
        position_y_joueur1 -= speed

    elif keys[pygame.K_s] and position_y_joueur1 + height_joueur1 < window_resolution[1]:  # Permettre au rectangle d'aller jusqu'en bas
        position_y_joueur1 += speed

    return position_y_joueur1

# Mouvement du joueur 2
def player2(position_y_joueur2, height_joueur2, window_resolution):
    keys = pygame.key.get_pressed()
    speed = 0.6  # Vitesse d'exécution

    if keys[pygame.K_UP] and position_y_joueur2 > 0:  # Eviter que le rectangle ne dépasse pas le haut de l'écran
        position_y_joueur2 -= speed

    elif keys[pygame.K_DOWN] and position_y_joueur2 + height_joueur2 < window_resolution[1]:  # Permettre au rectangle d'aller jusqu'en bas
        position_y_joueur2 += speed

    return position_y_joueur2




# Mouvement de la balle
def ball(ball_position_x, ball_position_y, ball_speed_x, ball_speed_y, width_joueur1, height_joueur1, position_x_joueur1, position_y_joueur1, position_x_joueur2, position_y_joueur2, window_resolution):
    
    # Gestion des collisions avec les bords de la fenêtre
    if ball_position_y - 20 <= 0 or ball_position_y + 20 >= window_resolution[1]:
        ball_speed_y = -ball_speed_y

    # Gestion des collisions avec la raquette du joueur 1
    if ball_position_x - 20 <= position_x_joueur1 + width_joueur1 and position_y_joueur1 <= ball_position_y <= position_y_joueur1 + height_joueur1:
        ball_speed_x = -ball_speed_x

    # Gestion des collisions avec la raquette du joueur 2
    elif ball_position_x + 20 >= position_x_joueur2 and position_y_joueur2 <= ball_position_y <= position_y_joueur2 + height_joueur1:
        ball_speed_x = -ball_speed_x


     # Gestion des buts
    if ball_position_x < 0 or ball_position_x > window_resolution[0] :
        
        # Engagement 

        ball_position_x = window_resolution[0] / 2  #  coordonnées du point central de la fenêtre
        ball_position_y = window_resolution[1] / 2  #  coordonnées du point central de la fenêtre
        ball_speed_x = -ball_speed_x  # Inversion de la direction de la balle pour le prochain coup     


    ball_position_x += ball_speed_x
    ball_position_y += ball_speed_y

    return ball_position_x, ball_position_y, ball_speed_x, ball_speed_y




def score(ball_position_x, window_resolution, score_joueur1, score_joueur2):

    if ball_position_x < 0 :
        score_joueur2 += 1

    elif ball_position_x > window_resolution[0] :
        score_joueur1 += 1
    
    return score_joueur1, score_joueur2






# Dessin des objets
def draw_objects(window_surface, white, red, position_x_joueur1, position_y_joueur1, width_joueur1, height_joueur1, position_x_joueur2, position_y_joueur2, width_joueur2, height_joueur2, ball_position_x, ball_position_y, ball_radius, window_resolution):
    window_surface.fill((0, 0, 0))  # Effacer l'écran avec du noir

    # Dessiner la ligne verticale au centre
    center_x = window_resolution[0] // 2
    pygame.draw.line(window_surface, white, (center_x, 0), (center_x, window_resolution[1]), 2)

    # Dessiner les joueurs et la balle
    pygame.draw.rect(window_surface, white, (position_x_joueur1, position_y_joueur1, width_joueur1, height_joueur1))  # Dessin du joueur 1
    pygame.draw.rect(window_surface, white, (position_x_joueur2, position_y_joueur2, width_joueur2, height_joueur2))  # Dessin du joueur 2
    pygame.draw.circle(window_surface, red, (int(ball_position_x), int(ball_position_y)), ball_radius)  # Dessin de la balle
    
    pygame.display.flip()


# Dessin du score
def draw_score(window_surface, font, score_joueur1, score_joueur2, white, window_resolution):
    # Créer les surfaces de texte pour les scores
    text_surface_joueur1 = font.render(f"{score_joueur1}", True, white)
    text_surface_joueur2 = font.render(f"{score_joueur2}", True, white)
    
    # Obtenir les largeurs des surfaces de texte
    width_joueur1 = text_surface_joueur1.get_width()
    width_joueur2 = text_surface_joueur2.get_width()
    
    # Calculer les positions pour centrer le texte
    total_width = width_joueur1 + width_joueur2 + 50  # Espacement de 50 pixels entre les scores
    center_x = window_resolution[0] // 2
    start_x = center_x - (total_width // 2)
    
    # Positionner les scores
    position_x_joueur1 = start_x
    position_x_joueur2 = start_x + width_joueur1 + 50  # Espacement de 50 pixels entre les scores

    # Afficher les scores
    window_surface.blit(text_surface_joueur1, (position_x_joueur1, 10))
    window_surface.blit(text_surface_joueur2, (position_x_joueur2, 10))

    pygame.display.flip()  # Rafraîchissement de l'affichage






def main():
    window_surface, window_resolution = init_game()

    # Couleur des objets
    white = (255, 255, 255)  # Couleur des scores et des objets
    red = (255, 0, 0)  # Balle

    # Valeurs et paramètres pour la balle
    ball_position_x = 420
    ball_position_y = 300
    ball_speed_x = 0.7
    ball_speed_y = 0.7
    ball_radius = 17  # Rayon

    # Modification des dimensions et positions des joueurs
    width_joueur1, height_joueur1 = 20, 150
    position_x_joueur1, position_y_joueur1 = 0, 225

    width_joueur2, height_joueur2 = 20, 150
    position_x_joueur2, position_y_joueur2 = window_resolution[0] - width_joueur2, 225

    # Initialisation des scores
    score_joueur1 = 0
    score_joueur2 = 0

    # Définir une police plus grande pour le score
    font = pygame.font.Font(None, 80)  # Taille de la police augmentée pour une meilleure visibilité

    # Boucle principale active pour la fenêtre
    launched = True
    while launched:
        launched = events()  # Gestion des événements

        # Mouvement des joueurs
        position_y_joueur1 = player1(position_y_joueur1, height_joueur1, window_resolution)
        position_y_joueur2 = player2(position_y_joueur2, height_joueur2, window_resolution)

        # Mouvement de la balle
        ball_position_x, ball_position_y, ball_speed_x, ball_speed_y = ball(
            ball_position_x, ball_position_y, ball_speed_x, ball_speed_y,
            width_joueur1, height_joueur1, position_x_joueur1, position_y_joueur1,
            position_x_joueur2, position_y_joueur2, window_resolution
        )
       
        # Affichage du score
        score_joueur1, score_joueur2 = score(ball_position_x, window_resolution, score_joueur1, score_joueur2)

        # Dessin des objets
        draw_objects(
            window_surface, white, red,
            position_x_joueur1, position_y_joueur1, width_joueur1, height_joueur1,
            position_x_joueur2, position_y_joueur2, width_joueur2, height_joueur2,
            ball_position_x, ball_position_y, ball_radius, window_resolution
        )
        draw_score(window_surface, font, score_joueur1, score_joueur2, white, window_resolution)

        pygame.display.flip()  # Rafraîchissement de l'affichage

        
if __name__ == "__main__":
    main()


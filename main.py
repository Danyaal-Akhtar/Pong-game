import pygame
from pygame.locals import *

from player import player
from ball import ball
from game import update_score
from effects import trail
from colors import ball_color
from start import start_screen


def init_game():
    pygame.init()
    window_resolution = (840, 600)
    window_surface = pygame.display.set_mode(window_resolution)
    pygame.display.set_caption("Pong Game")
    return window_surface, window_resolution


def handle_events():
    for event in pygame.event.get():
        if event.type == QUIT:
            return False
    return True


def main():
    window_surface, window_resolution = init_game()
    if not start_screen(window_surface, window_resolution):
        pygame.quit()
        return

    clock = pygame.time.Clock()

    white = (255, 255, 255)
    black = (0, 0, 0)

    width_joueur, height_joueur = 20, 150
    position_x_joueur1, position_y_joueur1 = 0, 225
    position_x_joueur2, position_y_joueur2 = window_resolution[0] - width_joueur, 225

    ball_position_x = window_resolution[0] / 2
    ball_position_y = window_resolution[1] / 2
    ball_speed_x = 6
    ball_speed_y = 6
    ball_radius = 17
    color_balle = ball_color()

    score_joueur1 = 0
    score_joueur2 = 0
    font = pygame.font.Font(None, 80)

    game_speed = 75
    max_speed = 120

    ball_history = []

    running = True
    while running:
        running = handle_events()

        position_y_joueur1 = player(
            position_y_joueur1, height_joueur, window_resolution, K_z, K_s
        )
        position_y_joueur2 = player(
            position_y_joueur2, height_joueur, window_resolution, K_UP, K_DOWN
        )

        (
            ball_position_x,
            ball_position_y,
            ball_speed_x,
            ball_speed_y,
            rebond
        ) = ball(
            ball_position_x,
            ball_position_y,
            ball_speed_x,
            ball_speed_y,
            width_joueur,
            height_joueur,
            position_x_joueur1,
            position_y_joueur1,
            position_x_joueur2,
            position_y_joueur2,
            window_resolution
        )

        if rebond:
            game_speed = min(game_speed + 2, max_speed)
            color_balle = ball_color()

        old_score_j1, old_score_j2 = score_joueur1, score_joueur2
        score_joueur1, score_joueur2 = update_score(
            ball_position_x,
            window_resolution[0],
            score_joueur1,
            score_joueur2
        )

        if score_joueur1 != old_score_j1 or score_joueur2 != old_score_j2:
            game_speed = 60
            ball_history.clear()

        ball_history.insert(0, (ball_position_x, ball_position_y))
        if len(ball_history) > 8:
            ball_history.pop()

        window_surface.fill(black)

        pygame.draw.line(
            window_surface,
            white,
            (window_resolution[0] // 2, 0),
            (window_resolution[0] // 2, window_resolution[1]),
            2
        )
        pygame.draw.rect(
            window_surface,
            white,
            (position_x_joueur1, position_y_joueur1, width_joueur, height_joueur)
        )
        pygame.draw.rect(
            window_surface,
            white,
            (position_x_joueur2, position_y_joueur2, width_joueur, height_joueur)
        )

        for i, pos in enumerate(ball_history):
            alpha = max(30, 150 - i * 20)
            radius = max(4, ball_radius - i * 2)
            trail(window_surface, pos, radius, color_balle, alpha)

        pygame.draw.circle(
            window_surface,
            color_balle,
            (int(ball_position_x), int(ball_position_y)),
            ball_radius
        )

        text_j1 = font.render(str(score_joueur1), True, white)
        text_j2 = font.render(str(score_joueur2), True, white)
        window_surface.blit(text_j1, (window_resolution[0] // 2 - 100, 10))
        window_surface.blit(text_j2, (window_resolution[0] // 2 + 60, 10))

        pygame.display.flip()
        clock.tick(game_speed)

    pygame.quit()


if __name__ == "__main__":
    main()

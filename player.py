import pygame

def player(position_y, height, window_resolution, key_up, key_down):
    keys = pygame.key.get_pressed()
    speed = 6

    if keys[key_up] and position_y > 0:
        position_y -= speed

    elif keys[key_down] and position_y + height < window_resolution[1]:
        position_y += speed

    return position_y

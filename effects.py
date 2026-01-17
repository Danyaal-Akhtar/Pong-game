import pygame

def trail(surface, position, radius, color, alpha):
    trail_surface = pygame.Surface((radius * 2, radius * 2), pygame.SRCALPHA)
    pygame.draw.circle(
        trail_surface,
        (*color, alpha),
        (radius, radius),
        radius
    )
    surface.blit(
        trail_surface,
        (position[0] - radius, position[1] - radius)
    )

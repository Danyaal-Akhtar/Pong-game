import pygame
from pygame.locals import *

def start_screen(window_surface, window_resolution):
  
    font = pygame.font.Font(None, 80)
    button_font = pygame.font.Font(None, 50)
    clock = pygame.time.Clock()
    running = True

    start_button = pygame.Rect(window_resolution[0]//2 - 100, window_resolution[1]//2 - 40, 200, 80)

    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                return False
            if event.type == MOUSEBUTTONDOWN:
                if start_button.collidepoint(event.pos):
                    return True 
     
        window_surface.fill((0, 0, 0))

 
        title_surface = font.render("PONG GAME", True, (255, 255, 255))
        window_surface.blit(title_surface, (window_resolution[0]//2 - title_surface.get_width()//2, 150))

      
        pygame.draw.rect(window_surface, (0, 200, 0), start_button)
        start_text = button_font.render("START", True, (255, 255, 255))
        window_surface.blit(start_text, (
            start_button.x + start_button.width//2 - start_text.get_width()//2,
            start_button.y + start_button.height//2 - start_text.get_height()//2
        ))

        pygame.display.flip()
        clock.tick(60)

import pytest
import pygame
import sys

@pytest.mark.parametrize("screen_width, screen_height", [(1200, 750)])
def test_game(screen_width, screen_height):
    pygame.init()
    screen = pygame.display.set_mode((screen_width, screen_height))
   
    ball = pygame.Rect(screen_width/2 - 15, screen_height/2 - 15, 30, 30)
    player = pygame.Rect(screen_width - 20, screen_height/2 - 50, 10, 100)
    opponent = pygame.Rect(10, screen_height/2 - 50, 10, 100)
    bg_color = pygame.Color('grey')
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        screen.fill((0, 0, 0))  
        pygame.draw.rect(screen, bg_color, player)
        pygame.draw.rect(screen, bg_color, opponent)
        pygame.draw.ellipse(screen, bg_color, ball)
        pygame.draw.aaline(screen, bg_color, (screen_width/2, 0), (screen_width/2, screen_height))

        pygame.display.flip()

    pygame.quit()

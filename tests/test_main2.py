import pygame
import sys
import pytest
from pong import ball_animation, player_animation, opponent_animation, ball_restart

@pytest.fixture
def screen():
    pygame.init()
    screen_width = 1200
    screen_height = 750
    screen = pygame.display.set_mode((screen_width, screen_height))
    yield screen
    pygame.quit()

def test_ball_movement(screen):
    ball_rect = pygame.Rect(screen.get_width() / 2 - 14, screen.get_height() / 2 - 14, 28, 28)
    ball_speed_x = 7
    ball_speed_y = 7
    ball_animation(ball_rect, ball_speed_x, ball_speed_y, screen.get_width(), screen.get_height())

def test_player_movement(screen):
    player_rect = pygame.Rect(screen.get_width() - 20, screen.get_height() / 2 - 70, 10, 140)
    player_speed = 7
    player_animation(player_rect, player_speed, screen.get_height())

def test_opponent_movement(screen):
    ball_rect = pygame.Rect(screen.get_width() / 2 - 14, screen.get_height() / 2 - 14, 28, 28)
    opponent_rect = pygame.Rect(10, screen.get_height() / 2 - 70, 10, 140)
    opponent_speed = 7
    opponent_animation(opponent_rect, ball_rect, opponent_speed, screen.get_height())

def test_ball_restart():
    ball_rect = pygame.Rect(screen.get_width() / 2 - 14, screen.get_height() / 2 - 14, 28, 28)
    ball_speed_x = 7
    ball_speed_y = 7
    ball_restart(ball_rect, ball_speed_x, ball_speed_y)


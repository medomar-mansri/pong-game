import unittest
import pygame
import sys
from pong import ball_animation, player_animation, opponent_animation, ball_restart

class TestPongGame(unittest.TestCase):

    def setUp(self):
        pygame.init()
        self.screen_width = 1200
        self.screen_height = 750
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.clock = pygame.time.Clock()

    def tearDown(self):
        pygame.quit()

    def test_ball_movement(self):
        ball_rect = pygame.Rect(self.screen_width / 2 - 14, self.screen_height / 2 - 14, 28, 28)
        ball_speed_x = 7
        ball_speed_y = 7
        ball_animation(ball_rect, ball_speed_x, ball_speed_y, self.screen_width, self.screen_height)
      
    def test_player_movement(self):
        player_rect = pygame.Rect(self.screen_width - 20, self.screen_height / 2 - 70, 10, 140)
        player_speed = 7
        player_animation(player_rect, player_speed, self.screen_height)
        

    def test_opponent_movement(self):
        ball_rect = pygame.Rect(self.screen_width / 2 - 14, self.screen_height / 2 - 14, 28, 28)
        opponent_rect = pygame.Rect(10, self.screen_height / 2 - 70, 10, 140)
        opponent_speed = 7
        opponent_animation(opponent_rect, ball_rect, opponent_speed, self.screen_height)
       
    def test_ball_restart(self):
        ball_rect = pygame.Rect(self.screen_width / 2 - 14, self.screen_height / 2 - 14, 28, 28)
        ball_speed_x = 7
        ball_speed_y = 7
        ball_restart(ball_rect, ball_speed_x, ball_speed_y)
       

if __name__ == '__main__':
    unittest.main()

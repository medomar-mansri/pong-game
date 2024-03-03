import unittest
import pygame
from pong import ball_animation, player_animation

class TestPongGame(unittest.TestCase):

    def setUp(self):
        pygame.init()
        self.screen_width = 1200
        self.screen_height = 750
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.clock = pygame.time.Clock()

    def tearDown(self):
        pygame.quit()

    def test_ball_animation(self):
        ball_rect = pygame.Rect(self.screen_width / 2 - 14, self.screen_height / 2 - 14, 28, 28)
        ball_speed_x = 7
        ball_speed_y = 7
        player_rect = pygame.Rect(self.screen_width - 20, self.screen_height / 2 - 70, 10, 140)
        opponent_rect = pygame.Rect(10, self.screen_height / 2 - 70, 10, 140)
        ball_animation(ball_rect, ball_speed_x, ball_speed_y, player_rect, opponent_rect, self.screen_width, self.screen_height)
        

    def test_player_animation(self):
        player_rect = pygame.Rect(self.screen_width - 20, self.screen_height / 2 - 70, 10, 140)
        player_speed = 7
        player_animation(player_rect, player_speed, self.screen_height)
        

if __name__ == '__main__':
    unittest.main()

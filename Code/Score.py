import pygame
from preferences import *


class Score:
    def __init__(self, p_num):
        self.font = pygame.font.SysFont('ariel.ttf', 72, True)
        self.x = SCREEN_WIDTH / 4 if p_num == 1 else SCREEN_WIDTH / 4 * 3
        self.y = SCREEN_HEIGHT / 6
        self.score = 0
        self.text = self.font.render(f"{self.score}", True, (255, 255, 255))
        self.rect = self.text.get_rect()
        self.rect.center = (self.x, self.y)

    def increase_score(self):
        self.score += 1
        self.text = self.font.render(f"{self.score}", True, (255, 255, 255))

    def reset_score(self):
        self.score = 0
        self.text = self.font.render(f"{self.score}", True, (255, 255, 255))

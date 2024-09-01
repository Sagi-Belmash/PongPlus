import pygame
import random
import os
from Ball import Ball
from stats import *


class Powerup:
    def __init__(self, name):
        self.x = random.randint(200, SCREEN_WIDTH - 200)
        self.y = random.randrange(50, SCREEN_HEIGHT - 50)
        self.name = name
        self.image = pygame.image.load(os.path.join(os.path.dirname(__file__), "../pics", self.name + ".png"))
        self.rect = pygame.rect.Rect(self.x, self.y, 40, 40)

    def action(self, b, game_time, balls=None):
        if self.name == "split":
            balls += [Ball(game_time, b.x, b.y, False) for _ in range(1)]
        elif self.name == "grow" and b.last_player is not None:
            b.last_player.grow()
        elif self.name == "shrink" and b.last_player is not None:
            b.last_player.shrink()
        elif self.name == "big_ball":
            b.grow()
        elif self.name == "small_ball":
            b.shrink()
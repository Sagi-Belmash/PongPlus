import time
import math
import random
import pygame
from Player import Player
from stats import *


class Ball:
    def __init__(self, game_time, x: float = SCREEN_WIDTH / 2, y: float = SCREEN_HEIGHT / 2, stop: bool = True):
        self.last_player: Player | None = None
        self.touch: str | Player | None = None
        self.x: float = x
        self.y: float = y
        direction: float = random.random() * math.pi / 2 - math.pi / 4
        self.x_speed: float = B_SPEED * math.cos(direction) * pow(-1, random.randint(1, 2))
        self.y_speed: float = B_SPEED * math.sin(direction)
        self.rect: pygame.Rect = pygame.Rect(self.x - B_RADIUS, self.y - B_RADIUS, B_RADIUS * 2, B_RADIUS * 2)
        headstart: int = 0 if stop else 2
        self.lock_timer: time = time.time() - headstart
        self.color: tuple = WHITE
        self.game_time: time = game_time
        self.radius: float = B_RADIUS
        self.effect_timer: time = 0

    def flip_x(self):
        self.x_speed *= -1

    def flip_y(self, touch):
        if touch != self.touch:
            self.y_speed *= -1
            self.touch = touch

    def move(self, dt):
        if time.time() - self.lock_timer > 2:
            self.x += self.x_speed * dt * ((time.time() - self.game_time) / 25 + 1)
            self.y += self.y_speed * dt * ((time.time() - self.game_time) / 25 + 1)

    def hit(self, player, p_num):
        d: int = 1 if p_num == 1 else -1
        if player != self.last_player:
            hp: float = (self.y - player.y) / player.height
            direction: float = math.pi / 2 * hp - math.pi / 4
            self.x_speed = B_SPEED * math.cos(direction) * d
            self.y_speed = B_SPEED * math.sin(direction)
            self.last_player = player
            self.touch = player

    def update(self):
        if time.time() - self.effect_timer > EFFECT_TIME:
            self.radius = B_RADIUS
        self.rect = pygame.rect.Rect(self.x - self.radius, self.y - self.radius, self.radius * 2, self.radius * 2)

    def grow(self):
        self.radius *= 2

    def shrink(self):
        self.radius /= 2

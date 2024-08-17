import time
import pygame
from preferences import *


class Player:
    def __init__(self, p_num: int):
        self.y: float = SCREEN_HEIGHT / 2 - P_HEIGHT / 2
        if p_num == 1:
            self.x: float = SCREEN_WIDTH / 10 + P_WIDTH / 2
        else:
            self.x: float = SCREEN_WIDTH / 10 * 9 - P_WIDTH / 2
        self.height: float = P_HEIGHT
        self.rect: pygame.rect.Rect = pygame.rect.Rect(self.x, self.y, P_WIDTH, self.height)
        self.lock_timer: time = time.time()
        self.effect_timer: time = time.time()

    def move_left(self, dt):
        if time.time() - self.lock_timer > 2:
            self.x -= P_SPEED * dt

    def move_right(self, dt):
        if time.time() - self.lock_timer > 2:
            self.x += P_SPEED * dt

    def move_up(self, dt):
        if time.time() - self.lock_timer > 2:
            self.y -= P_SPEED * dt

    def move_down(self, dt):
        if time.time() - self.lock_timer > 2:
            self.y += P_SPEED * dt

    def update(self):
        # Restoring size after effect ended
        if time.time() - self.effect_timer > EFFECT_TIME and self.height != P_HEIGHT:
            self.y += (self.height - P_HEIGHT) / 2
            self.height = P_HEIGHT

        self.rect: pygame.Rect = pygame.Rect(self.x, self.y, P_WIDTH, self.height)

    def grow(self):
        self.effect_timer: time = time.time()
        self.height *= 1.5
        self.y -= P_HEIGHT * 0.25

    def shrink(self):
        self.effect_timer: time = time.time()
        self.height *= 0.5
        self.y += P_HEIGHT * 0.25

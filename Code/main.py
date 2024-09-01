import random
import time
import pygame
import Ball
import game
from Ball import Ball
from Score import Score
from Player import Player
from Powerup import Powerup
from stats import *


def draw(p1=None, p2=None, powerups=None,
         s1=None, s2=None, balls=None, dots=False, start=False):
    # Draw Screen
    pygame.display.flip()
    screen.blit(surface, (0, 0))
    surface.fill(BLACK)
    # Draw Players
    if p1 is not None and p2 is not None:
        pygame.draw.rect(screen, WHITE, p1.rect)
        pygame.draw.rect(screen, WHITE, p2.rect)
    # Draw Powerups
    if powerups is not None:
        for p in powerups:
            screen.blit(p.image, (p.x, p.y))
    # Draw Scores
    if s1 is not None and s2 is not None:
        surface.blit(s1.text, s1.rect)
        surface.blit(s2.text, s2.rect)
    # Draw Balls
    if balls is not None:
        for b in balls:
            pygame.draw.circle(surface, b.color, (b.x, b.y), b.radius)
    # Draw center line
    if dots:
        dx = SCREEN_WIDTH / 2
        dy = SCREEN_HEIGHT
        while dy > 0:
            DOT_SIZE = 2
            dot = pygame.rect.Rect(dx - DOT_SIZE / 2, dy, DOT_SIZE, DOT_SIZE)
            pygame.draw.rect(screen, WHITE, dot)
            dy -= 7
    if start:
        surface.blit(start_text, start_rect)


def pause():
    while True:

        if pygame.key.get_pressed()[pygame.K_ESCAPE]:
            break


def hit(score) -> bool:
    score.increase_score()
    if score.score == MAX_POINTS:
        return True
    return False


def main():

    # Score creating
    s1: Score = Score(1)
    s2: Score = Score(2)
    # Game run

    running: bool = True
    focused = True
    start = False

    active_powerups: list[Powerup] | None = None
    game_time = 0
    while running:
        # Start screen
        if not start:
            draw(start=True)
            if pygame.key.get_pressed()[pygame.K_RETURN]:
                start: bool = True
                game_time: float = time.time() - 1

                # Player creating
                p1: Player = Player(1)
                p2: Player = Player(2)

                # Ball creating
                balls: list[Ball] = [Ball(game_time)]

                # Temp powerup
                active_powerups = []
        # Game
        else:
            dt = clock.tick(FPS) / 1000
            if focused:
                draw(p1, p2, active_powerups, s1, s2, balls, True)

                # Update players
                p1.update()
                p2.update()

                # Ball management
                for b in balls:
                    b.update()
                    # Check colling with players
                    if b.rect.colliderect(p1.rect):
                        b.x = p1.x + P_WIDTH + B_RADIUS
                    elif b.rect.colliderect(p2.rect):
                        b.x = p2.x - B_RADIUS
                    # Ball movement
                    b.move(dt if dt < 0.1 else 0)
                    if b.x + B_RADIUS >= SCREEN_WIDTH or b.x - B_RADIUS <= 0:
                        s = s1 if b.x + B_RADIUS >= SCREEN_WIDTH else s2
                        if hit(s):
                            # End text
                            end_text = (middle_screen_font
                                        .render(f"The winner is Player {1 if s1.score == MAX_POINTS else 2}!",
                                                True, WHITE))
                            end_rect = end_text.get_rect()
                            end_rect.center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 50)
                            # Second end text
                            fuck_u_font = pygame.font.SysFont('arial', 100, True)
                            fuck_u_text = (fuck_u_font.render(f"F@#K YOU PLAYER {2 if s1.score == MAX_POINTS else 1}!",
                                                              True, WHITE))
                            fuck_u_rect = fuck_u_text.get_rect()
                            fuck_u_rect.center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 50)
                            # Draw end screen
                            surface.fill(BLACK)
                            surface.blit(end_text, end_rect)
                            pygame.draw.rect(surface, WHITE, p1.rect)
                            pygame.draw.rect(surface, WHITE, p2.rect)
                            surface.blit(s1.text, s1.rect)
                            surface.blit(s2.text, s2.rect)
                            pygame.display.flip()
                            pygame.time.wait(3000)
                            surface.blit(fuck_u_text, fuck_u_rect)
                            screen.blit(surface, (0, 0))
                            pygame.display.flip()
                            pygame.time.wait(2000)
                            s1.reset_score()
                            s2.reset_score()
                            start = False
                        p1 = Player(1)
                        p2 = Player(2)
                        active_powerups = []
                        game_time = time.time() - 1
                        balls = [Ball(game_time)]
                        continue
                    if b.y + B_RADIUS >= SCREEN_HEIGHT:
                        b.flip_y("f")
                    if b.y - B_RADIUS <= 0:
                        b.flip_y("c")
                    if p1.rect.colliderect(b.rect):
                        b.hit(p1, 1)
                    if p2.rect.colliderect(b.rect):
                        b.hit(p2, 2)
                    for p in active_powerups:
                        if b.rect.colliderect(p.rect):
                            p.action(b, game_time, balls)
                            active_powerups.pop(active_powerups.index(p))

                # Generate power-ups
                if active_powerups.__len__() < 3 and not random.randint(0, 99) % 100:
                    active_powerups += [Powerup(POWER_UPS[random.randint(0, len(POWER_UPS) - 1)])]

                # Game keys
                keys = pygame.key.get_pressed()
                if keys[pygame.K_w] and p1.y > 0:
                    p1.move_up(dt)
                if keys[pygame.K_s] and p1.y < SCREEN_HEIGHT - P_HEIGHT:
                    p1.move_down(dt)
                if keys[pygame.K_a] and p1.x > 0:
                    p1.move_left(dt)
                if keys[pygame.K_d] and p1.x < SCREEN_WIDTH / 2 - P_WIDTH:
                    p1.move_right(dt)
                if keys[pygame.K_UP] and p2.y > 0:
                    p2.move_up(dt)
                if keys[pygame.K_DOWN] and p2.y < SCREEN_HEIGHT - P_HEIGHT:
                    p2.move_down(dt)
                if keys[pygame.K_LEFT] and p2.x > SCREEN_WIDTH / 2:
                    p2.move_left(dt)
                if keys[pygame.K_RIGHT] and p2.x < SCREEN_WIDTH - P_WIDTH:
                    p2.move_right(dt)
                if keys[pygame.K_ESCAPE]:
                    pause()


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.ACTIVEEVENT:
                focused = not focused

    pygame.quit()


if __name__ == "__main__":
    main()

import pygame

SCREEN_WIDTH: int = 1200
SCREEN_HEIGHT: int = 600

P_WIDTH: int = 20
P_HEIGHT: int = 120
B_RADIUS: int = 10

P_SPEED: float = 600
B_SPEED: float = 600
FPS: int = 120

WHITE: tuple[int, int, int] = (255, 255, 255)
BLACK: tuple[int, int, int] = (0, 0, 0)

MAX_POINTS: int = 2

POWER_UPS: list[str] = ["split", "grow", "shrink", "big_ball", "small_ball"]

EFFECT_TIME: float = 5
EFFECT_CHANCE: float = 100

# Init
pygame.init()


dt: float = 0
clock: pygame.time.Clock = pygame.time.Clock()

screen: pygame.display = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
surface: pygame.Surface = pygame.Surface(screen.get_size())

# Start text
middle_screen_font = pygame.font.SysFont('ariel.ttf', 72)
start_text = middle_screen_font.render("Press ENTER to start the game", True, WHITE)
start_rect = start_text.get_rect()
start_rect.center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 640, 480
PLAYER_SIZE = 30
GRAVITY = 1
JUMP_STRENGTH = 20
MOVE_SPEED = 5

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Screen Setup
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Mini Jump King")

# Player Setup
player = pygame.Rect(SCREEN_WIDTH // 2, SCREEN_HEIGHT - PLAYER_SIZE, PLAYER_SIZE, PLAYER_SIZE)
player_velocity_y = 0
player_velocity_x = 0
on_ground = True

# Game Loop
clock = pygame.time.Clock()
while True:
    # Event Handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and on_ground:
                player_velocity_y = -JUMP_STRENGTH
                on_ground = False
            if event.key == pygame.K_LEFT:
                player_velocity_x = -MOVE_SPEED
            if event.key == pygame.K_RIGHT:
                player_velocity_x = MOVE_SPEED
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT and player_velocity_x < 0:
                player_velocity_x = 0
            if event.key == pygame.K_RIGHT and player_velocity_x > 0:
                player_velocity_x = 0

    # Physics
    player.y += player_velocity_y
    player.x += player_velocity_x
    player_velocity_y += GRAVITY

    # Boundary Checking for Player
    if player.x < 0:
        player.x = 0
    if player.x > SCREEN_WIDTH - PLAYER_SIZE:
        player.x = SCREEN_WIDTH - PLAYER_SIZE

    # Check Ground
    if player.y >= SCREEN_HEIGHT - PLAYER_SIZE:
        player.y = SCREEN_HEIGHT - PLAYER_SIZE
        player_velocity_y = 0
        on_ground = True

    # Drawing
    screen.fill(WHITE)
    pygame.draw.rect(screen, BLACK, player)
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

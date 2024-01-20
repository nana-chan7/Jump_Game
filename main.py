import pygame
import sys

# 初期化
pygame.init()

# 設定
SCREEN_WIDTH, SCREEN_HEIGHT = 480, 720  # 画面サイズ
# プレイヤー設定
P_SIZE_X = 15  # 横幅
P_SIZE_Y = 30  # 縦幅
GRAVITY = 1
JUMP_POWER = 20

# 色設定
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# 画面
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Mini Jump Game")

# プレイヤー
player = pygame.Rect(SCREEN_WIDTH // 2, SCREEN_HEIGHT - P_SIZE_Y, P_SIZE_X, P_SIZE_Y)
player_velocity = 0
on_ground = True

# メイン処理
clock = pygame.time.Clock()
while True:
    # イベント処理
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and on_ground:
                player_velocity = -JUMP_POWER
                on_ground = False

    player.y += player_velocity
    player_velocity += GRAVITY

    # 着地していたら、
    if player.y >= SCREEN_HEIGHT - P_SIZE_Y:
        player.y = SCREEN_HEIGHT - P_SIZE_Y
        player_velocity = 0
        on_ground = True

    # 描画
    screen.fill(WHITE)
    pygame.draw.rect(screen, BLACK, player)
    pygame.display.flip()

    # フレームレート
    clock.tick(60)

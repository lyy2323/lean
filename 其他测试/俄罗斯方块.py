import pygame
import random

# 初始化pygame
pygame.init()

# 定义颜色
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
COLORS = [
    (0, 255, 255),  # 青色
    (255, 255, 0),  # 黄色
    (255, 165, 0),  # 橙色
    (0, 0, 255),    # 蓝色
    (0, 255, 0),    # 绿色
    (255, 0, 0),    # 红色
    (128, 0, 128)   # 紫色
]

# 定义屏幕大小
SCREEN_WIDTH = 300
SCREEN_HEIGHT = 600
BLOCK_SIZE = 30

# 定义游戏区域大小
PLAY_WIDTH = 10  # 10 blocks wide
PLAY_HEIGHT = 20  # 20 blocks tall

# 初始化屏幕
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("俄罗斯方块")

# 定义形状
SHAPES = [
    [[1, 1, 1, 1]],  # I
    [[1, 1, 1], [0, 1, 0]],  # T
    [[1, 1], [1, 1]],  # O
    [[1, 1, 0], [0, 1, 1]],  # S
    [[0, 1, 1], [1, 1, 0]],  # Z
    [[1, 1, 1], [1, 0, 0]],  # L
    [[1, 1, 1], [0, 0, 1]]   # J
]

# 定义游戏区域
grid = [[BLACK for _ in range(PLAY_WIDTH)] for _ in range(PLAY_HEIGHT)]

# 定义当前方块
current_piece = random.choice(SHAPES)
current_color = random.choice(COLORS)
current_x = PLAY_WIDTH // 2 - len(current_piece[0]) // 2
current_y = 0

# 定义游戏时钟
clock = pygame.time.Clock()

# 定义下落速度
fall_time = 0
fall_speed = 0.3

# 检查方块是否可以移动
def can_move(piece, x, y):
    for i, row in enumerate(piece):
        for j, cell in enumerate(row):
            if cell:
                if x + j < 0 or x + j >= PLAY_WIDTH or y + i >= PLAY_HEIGHT or grid[y + i][x + j] != BLACK:
                    return False
    return True

# 将方块固定到游戏区域
def lock_piece(piece, x, y):
    for i, row in enumerate(piece):
        for j, cell in enumerate(row):
            if cell:
                grid[y + i][x + j] = current_color

# 清除满行
def clear_lines():
    full_lines = []
    for i, row in enumerate(grid):
        if all(cell != BLACK for cell in row):
            full_lines.append(i)
    for i in full_lines:
        del grid[i]
        grid.insert(0, [BLACK for _ in range(PLAY_WIDTH)])

# 绘制游戏区域
def draw_grid():
    for i in range(PLAY_HEIGHT):
        for j in range(PLAY_WIDTH):
            pygame.draw.rect(screen, grid[i][j], (j * BLOCK_SIZE, i * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE), 0)
    for i in range(PLAY_HEIGHT):
        pygame.draw.line(screen, GRAY, (0, i * BLOCK_SIZE), (SCREEN_WIDTH, i * BLOCK_SIZE))
    for j in range(PLAY_WIDTH):
        pygame.draw.line(screen, GRAY, (j * BLOCK_SIZE, 0), (j * BLOCK_SIZE, SCREEN_HEIGHT))

# 绘制当前方块
def draw_piece(piece, x, y):
    for i, row in enumerate(piece):
        for j, cell in enumerate(row):
            if cell:
                pygame.draw.rect(screen, current_color, ((x + j) * BLOCK_SIZE, (y + i) * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE), 0)

# 游戏主循环
running = True
while running:
    screen.fill(BLACK)
    fall_time += clock.get_rawtime()
    clock.tick()

    if fall_time / 1000 >= fall_speed:
        fall_time = 0
        if can_move(current_piece, current_x, current_y + 1):
            current_y += 1
        else:
            lock_piece(current_piece, current_x, current_y)
            clear_lines()
            current_piece = random.choice(SHAPES)
            current_color = random.choice(COLORS)
            current_x = PLAY_WIDTH // 2 - len(current_piece[0]) // 2
            current_y = 0
            if not can_move(current_piece, current_x, current_y):
                running = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if can_move(current_piece, current_x - 1, current_y):
                    current_x -= 1
            if event.key == pygame.K_RIGHT:
                if can_move(current_piece, current_x + 1, current_y):
                    current_x += 1
            if event.key == pygame.K_DOWN:
                if can_move(current_piece, current_x, current_y + 1):
                    current_y += 1
            if event.key == pygame.K_UP:
                rotated_piece = list(zip(*current_piece[::-1]))
                if can_move(rotated_piece, current_x, current_y):
                    current_piece = rotated_piece

    draw_grid()
    draw_piece(current_piece, current_x, current_y)
    pygame.display.update()

pygame.quit()

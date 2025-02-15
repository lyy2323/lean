import pygame
import random

# 定义常量
WIDTH = 10  # 游戏区域宽度
HEIGHT = 20  # 游戏区域高度
BLOCK_SIZE = 30  # 每个方块的大小
FPS = 30  # 帧率
COLORS = [
    (255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0),
    (255, 0, 255), (0, 255, 255), (128, 0, 128)
]
SHAPES = [
    [[1, 1, 1, 1]],  # I
    [[1, 1, 1], [0, 1, 0]],  # T
    [[1, 1, 0], [0, 1, 1]],  # Z
    [[0, 1, 1], [1, 1, 0]],  # S
    [[1, 1, 1], [1, 0, 0]],  # L
    [[1, 1, 1], [0, 0, 1]],  # J
    [[1, 1], [1, 1]]   # O
]

# 初始化 Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH * BLOCK_SIZE, HEIGHT * BLOCK_SIZE))
pygame.display.set_caption("俄罗斯方块")
clock = pygame.time.Clock()

# 定义方块类
class Block:
    def __init__(self, x, y, shape):
        self.x = x
        self.y = y
        self.shape = shape
        self.color = random.choice(COLORS)

    def rotate(self):
        self.shape = list(zip(*self.shape[::-1]))

    def draw(self, surface):
        for i, row in enumerate(self.shape):
            for j, cell in enumerate(row):
                if cell:
                    pygame.draw.rect(surface, self.color, (
                        (self.x + j) * BLOCK_SIZE, (self.y + i) * BLOCK_SIZE,
                        BLOCK_SIZE, BLOCK_SIZE
                    ))

# 游戏主循环
def game():
    grid = [[0] * WIDTH for _ in range(HEIGHT)]
    current_block = Block(WIDTH // 2 - 2, 0, random.choice(SHAPES))
    game_over = False

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    current_block.x -= 1
                if event.key == pygame.K_RIGHT:
                    current_block.x += 1
                if event.key == pygame.K_DOWN:
                    current_block.y += 1
                if event.key == pygame.K_UP:
                    current_block.rotate()

        # 碰撞检测（边界和底部）
        if current_block.x < 0 or current_block.x + len(current_block.shape[0]) > WIDTH:
            current_block.x = max(0, min(current_block.x, WIDTH - len(current_block.shape[0])))
        if current_block.y + len(current_block.shape) > HEIGHT:
            current_block.y = HEIGHT - len(current_block.shape)
            # 将方块固定到网格
            for i, row in enumerate(current_block.shape):
                for j, cell in enumerate(row):
                    if cell:
                        grid[current_block.y + i][current_block.x + j] = current_block.color
            current_block = Block(WIDTH // 2 - 2, 0, random.choice(SHAPES))

        # 绘制
        screen.fill((0, 0, 0))
        current_block.draw(screen)
        for y, row in enumerate(grid):
            for x, color in enumerate(row):
                if color:
                    pygame.draw.rect(screen, color, (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    game()
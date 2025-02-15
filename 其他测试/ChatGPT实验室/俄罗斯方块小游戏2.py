import pygame
import random

# 初始化pygame
pygame.init()

# 定义常量
SCREEN_WIDTH = 300
SCREEN_HEIGHT = 600
BLOCK_SIZE = 30
GAME_SPEED = 500  # 游戏速度，单位为毫秒
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
COLORS = [
    (0, 255, 255),  # 青色
    (255, 165, 0),  # 橙色
    (255, 255, 0),  # 黄色
    (0, 0, 255),  # 蓝色
    (0, 255, 0),  # 绿色
    (255, 0, 0),  # 红色
    (128, 0, 128),  # 紫色
]

# 定义方块形状
SHAPES = [
    [[1, 1, 1, 1]],  # I形
    [[1, 1], [1, 1]],  # O形
    [[1, 1, 0], [0, 1, 1]],  # S形
    [[0, 1, 1], [1, 1, 0]],  # Z形
    [[1, 1, 1], [0, 1, 0]],  # T形
    [[1, 0, 0], [1, 1, 1]],  # L形
    [[0, 0, 1], [1, 1, 1]],  # J形
]

# 初始化屏幕
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('俄罗斯方块')

# 游戏状态
clock = pygame.time.Clock()


def draw_board(board):
    """绘制游戏面板"""
    for y in range(len(board)):
        for x in range(len(board[y])):
            if board[y][x]:
                pygame.draw.rect(screen, board[y][x], (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
            pygame.draw.rect(screen, WHITE, (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE), 1)


def check_collision(board, shape, offset):
    """检查是否发生碰撞"""
    off_x, off_y = offset
    for y, row in enumerate(shape):
        for x, cell in enumerate(row):
            if cell:
                if x + off_x < 0 or x + off_x >= len(board[0]) or y + off_y >= len(board):
                    return True
                if y + off_y >= 0 and board[y + off_y][x + off_x]:
                    return True
    return False


def clear_lines(board):
    """清除填满的行"""
    full_lines = [index for index, row in enumerate(board) if all(cell for cell in row)]
    for index in full_lines:
        del board[index]
        board.insert(0, [0] * len(board[0]))
    return len(full_lines)


def rotate(shape):
    """旋转方块"""
    return [list(row) for row in zip(*shape[::-1])]


def draw_text(text, font, color, surface, x, y):
    """绘制文本"""
    label = font.render(text, 1, color)
    surface.blit(label, (x, y))


def main():
    """游戏主函数"""
    board = [[0] * (SCREEN_WIDTH // BLOCK_SIZE) for _ in range(SCREEN_HEIGHT // BLOCK_SIZE)]
    current_shape = random.choice(SHAPES)
    current_color = random.choice(COLORS)
    current_pos = [5, 0]  # 起始位置

    running = True
    game_over = False
    score = 0

    font = pygame.font.SysFont('Arial', 30)

    while running:
        screen.fill(BLACK)

        # 处理事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and not game_over:
                if event.key == pygame.K_LEFT:
                    if not check_collision(board, current_shape, [current_pos[0] - 1, current_pos[1]]):
                        current_pos[0] -= 1
                if event.key == pygame.K_RIGHT:
                    if not check_collision(board, current_shape, [current_pos[0] + 1, current_pos[1]]):
                        current_pos[0] += 1
                if event.key == pygame.K_DOWN:
                    if not check_collision(board, current_shape, [current_pos[0], current_pos[1] + 1]):
                        current_pos[1] += 1
                if event.key == pygame.K_UP:
                    rotated_shape = rotate(current_shape)
                    if not check_collision(board, rotated_shape, current_pos):
                        current_shape = rotated_shape

        # 方块下落
        if not check_collision(board, current_shape, [current_pos[0], current_pos[1] + 1]):
            current_pos[1] += 1
        else:
            for y, row in enumerate(current_shape):
                for x, cell in enumerate(row):
                    if cell:
                        board[current_pos[1] + y][current_pos[0] + x] = current_color
            score += clear_lines(board)
            current_shape = random.choice(SHAPES)
            current_color = random.choice(COLORS)
            current_pos = [5, 0]

            if check_collision(board, current_shape, current_pos):
                game_over = True

        # 绘制面板和当前方块
        draw_board(board)
        for y, row in enumerate(current_shape):
            for x, cell in enumerate(row):
                if cell:
                    pygame.draw.rect(screen, current_color, (
                    (current_pos[0] + x) * BLOCK_SIZE, (current_pos[1] + y) * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))

        # 显示分数
        draw_text(f"Score: {score}", font, WHITE, screen, 10, 10)

        # 游戏结束
        if game_over:
            draw_text("Game Over!", font, WHITE, screen, SCREEN_WIDTH // 4, SCREEN_HEIGHT // 3)

        pygame.display.flip()
        clock.tick(5)

    pygame.quit()


if __name__ == "__main__":
    main()

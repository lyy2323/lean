import pygame
import random

# 初始化pygame
pygame.init()

# 定义颜色
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# 定义屏幕大小
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# 初始化屏幕
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("弹球游戏")

# 定义球类
class Ball:
    def __init__(self):
        self.radius = 10
        self.x = SCREEN_WIDTH // 2
        self.y = SCREEN_HEIGHT // 2
        self.speed_x = random.choice([-4, 4])
        self.speed_y = random.choice([-4, 4])
        self.color = RED

    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y

        # 碰撞检测
        if self.x - self.radius <= 0 or self.x + self.radius >= SCREEN_WIDTH:
            self.speed_x = -self.speed_x
        if self.y - self.radius <= 0:
            self.speed_y = -self.speed_y

    def draw(self):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

# 定义挡板类
class Paddle:
    def __init__(self):
        self.width = 100
        self.height = 10
        self.x = (SCREEN_WIDTH - self.width) // 2
        self.y = SCREEN_HEIGHT - 50
        self.speed = 0
        self.color = GREEN

    def move(self):
        self.x += self.speed
        if self.x < 0:
            self.x = 0
        elif self.x + self.width > SCREEN_WIDTH:
            self.x = SCREEN_WIDTH - self.width

    def draw(self):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

# 初始化球和挡板
ball = Ball()
paddle = Paddle()

# 定义游戏时钟
clock = pygame.time.Clock()

# 游戏主循环
running = True
while running:
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                paddle.speed = -5
            if event.key == pygame.K_RIGHT:
                paddle.speed = 5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                paddle.speed = 0

    # 移动球和挡板
    ball.move()
    paddle.move()

    # 检测球和挡板的碰撞
    if (ball.y + ball.radius >= paddle.y and
        ball.x >= paddle.x and ball.x <= paddle.x + paddle.width):
        ball.speed_y = -ball.speed_y

    # 检测球是否落地
    if ball.y + ball.radius >= SCREEN_HEIGHT:
        running = False

    # 绘制球和挡板
    ball.draw()
    paddle.draw()

    # 更新屏幕
    pygame.display.update()

    # 控制游戏帧率
    clock.tick(60)

pygame.quit()
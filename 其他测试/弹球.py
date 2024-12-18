import pygame
import random

# 初始化pygame
pygame.init()

# 游戏窗口尺寸
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))  # 创建游戏窗口
pygame.display.set_caption("弹球小游戏")  # 设置窗口标题

# 颜色定义
WHITE = (255, 255, 255)  # 白色，用于背景
BLUE = (0, 0, 255)  # 蓝色，用于绘制球
RED = (255, 0, 0)  # 红色，用于绘制障碍物

# 球和障碍物的属性
ball_radius = 15  # 球的半径
ball_pos = [WIDTH // 2, HEIGHT // 2]  # 球的初始位置，设置在窗口中央
ball_speed = [random.choice([-4, 4]), random.choice([-4, 4])]  # 球的速度，随机选择方向

obstacle_width = 100  # 障碍物的宽度
obstacle_height = 10  # 障碍物的高度
obstacle_pos = [random.randint(0, WIDTH - obstacle_width), random.randint(0, HEIGHT - 50)]  # 障碍物的初始位置，随机设置

# 游戏主循环
running = True
while running:
    # 处理事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # 如果用户点击关闭按钮，退出循环
            running = False

    # 更新球的位置
    ball_pos[0] += ball_speed[0]  # 更新球的水平位置
    ball_pos[1] += ball_speed[1]  # 更新球的垂直位置

    # 碰撞检测 - 窗口边界
    if ball_pos[0] <= ball_radius or ball_pos[0] >= WIDTH - ball_radius:  # 碰到左右边界，反向运动
        ball_speed[0] = -ball_speed[0]
    if ball_pos[1] <= ball_radius or ball_pos[1] >= HEIGHT - ball_radius:  # 碰到上下边界，反向运动
        ball_speed[1] = -ball_speed[1]

    # 碰撞检测 - 障碍物
    if (obstacle_pos[0] < ball_pos[0] < obstacle_pos[0] + obstacle_width and
        obstacle_pos[1] < ball_pos[1] + ball_radius < obstacle_pos[1] + obstacle_height):  # 检测球是否碰到障碍物
        ball_speed[1] = -ball_speed[1]  # 如果碰到障碍物，垂直方向反向运动

    # 绘制场景
    screen.fill(WHITE)  # 填充背景颜色
    pygame.draw.circle(screen, BLUE, ball_pos, ball_radius)  # 绘制球
    pygame.draw.rect(screen, RED, (obstacle_pos[0], obstacle_pos[1], obstacle_width, obstacle_height))  # 绘制障碍物

    # 刷新屏幕
    pygame.display.flip()  # 更新显示内容
    pygame.time.delay(30)  # 延迟，以控制游戏帧率

# 退出pygame
pygame.quit()  # 关闭游戏窗口
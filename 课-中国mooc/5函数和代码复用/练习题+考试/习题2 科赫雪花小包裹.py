import turtle
def koch(size, n):  # 定义一个“koch”的函数（两个参数分别是长度和阶数）
    if n == 0:  # 当n=0，即当递归到达最底层（阶数等于0时）
        turtle.fd(size)  # 海龟向前走长度为size的直线
    else:  # 如果n不等于0
        for angle in [0, 60, -120, 60]:  # 则遍历列表[0，60，-120,60]（后面用angle表示）
            turtle.left(angle)  # 遍历的情况下，海龟分别向左转上面遍历的角度（0，60，-120，60度）
            koch(size/3, n-1)  # 并且koch的长度除以3，阶数-1
def main(level):  # 定义一个“main”的函数，参数为“level”，这个函数执行以下操作：
    turtle.setup(600, 600)  # 制作一个600*600像素的画布
    turtle.penup()  # 抬起海龟画笔
    turtle.goto(-200,100)  # 向后和向上移动200和100像素
    turtle.pendown()  # 落下画笔
    turtle.pensize(2)  # 笔触大小为2像素
    koch(400,level)  # 运行上面的koch函数，其中给出长度参数为400，阶数没有给（暂时定义为“level”，应该是留在后面给的）
    turtle.right(120)  # 右转120度
    koch(400,level)  # 继续运行上面的koch函数，依然给出长度参数为400，阶数为level
    turtle.right(120)  # 右转120度
    koch(400,level)  # 继续运行上面的koch函数，依然给出长度参数为400，阶数为level
    turtle.hideturtle()  # 隐藏海龟画笔
    turtle.done()
try:  # 尝试
    level = eval(input('请输入科赫曲线的阶：'))  # level为上面的阶数参数，这里由用户自己输入，前面的eval是将输入的字符串转为数字，同时这样也要求用户必须输入数字
    main(level)  # 则运行上面的main函数，参数为用户输入的值
except:  # 如果用户输入的不是数字（这里靠eval来判断）
    print('输入错误')  # 则给除提示
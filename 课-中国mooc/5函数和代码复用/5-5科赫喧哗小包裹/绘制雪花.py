import turtle  # 调用turtle库
def koch(size, n):  # 定义函数koch，设置长度参数size和递归乘阶数为n
    if n == 0:  # 如果n等于0
        turtle.fd(size)  # 则向前size长裤
    else:  # 如果不等于0
        for angle in [0, 60, -120, 60]:  # 则遍历angle列表[0,60,-120,60]
            turtle.left(angle)  # 右转angle度（依次按列表中4个数字，第一次0度，第二次60度，第三次-120度，第四次60度）
            koch(size/3, n-1)  # 按长度除以3，阶数减去1的参数运行前面的函数
def main():  # 定义函数main，没有参数
    turtle.setup(600, 600)  # 制作一个600*600像素的画布
    turtle.penup()  # 提起海龟画笔
    turtle.goto(-200, 100)  # 从画笔初始的中间位置移动x坐标-200y坐标100个像素
    turtle.pendown()  # 落下画笔
    turtle.pensize(2)  # 笔触大小2像素
    level = 3  # 赋值level变量为3像素
    koch(400, level)  # 运行函数koch，长度400像素，阶乘level（即3像素）
    turtle.right(120)  # 右转120度
    koch(400,level)  # 运行函数koch，长度400像素，阶乘level（即3像素）
    turtle.right(120)  # 右转120度
    koch(400, level)  # 运行函数koch，长度400像素，阶乘level（即3像素）
    turtle.hideturtle()  # 隐藏画笔
    turtle.done()  # 画布停留
main()  # 运行函数main
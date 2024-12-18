import turtle as t  # 调用turtle库并起一个别名为t
import time  # 条用time库
def drawGap():  # 定义函数，绘制数码管的间隔，函数做如下操作
    t.penup()  # 提起海龟画笔
    t.fd(5)  # 向前5个像素

def drawLine(draw):  # 定义函数，绘制单段数码管，函数执行如下操作
    drawGap()  # 运行前面的函数drawGap
    t.pendown() if draw else t.penup()  # 根据draw的布尔值，决定是否则放下画笔，如果draw为True时候放下，否则penup
    t.fd(40)  # 前进40像素
    drawGap()  # 运行函数drawGap
    t.right(90)  # 右转90度

def drawDigit(d):  # 定义函数，执行下面操作，根据数字绘制七段数码管
    drawLine(True) if d in [2,3,4,5,6,8,9] else drawLine(False)  # 这是在绘制第1段数码管，如果d在右侧列表中，则判断为正确，运行drawLine函数的t.pendown，否则判断为错误，执行函数种drawLine的t.penup
    drawLine(True) if d in [0,1,3,4,5,6,7,8,9] else drawLine(False)  # 这是在绘制第2段数码管，如果d在右侧列表中，则判断为正确，运行drawLine函数的t.pendown，否则判断为错误，执行函数种drawLine的t.penup
    drawLine(True) if d in [0,2,3,5,6,8,9] else drawLine(False)  # 这是在绘制第3段数码管，如果d在右侧列表中，则判断为正确，运行drawLine函数的t.pendown，否则判断为错误，执行函数种drawLine的t.penup
    drawLine(True) if d in [0,2,6,8] else drawLine(False)  # 这是在绘制第4段数码管，如果d在右侧列表中，则判断为正确，运行drawLine函数的t.pendown，否则判断为错误，执行函数种drawLine的t.penup
    t.left(90)  # 左转90度
    drawLine(True) if d in [0,4,5,6,8,9] else drawLine(False)  # 这是在绘制第5段数码管，如果d在右侧列表中，则判断为正确，运行drawLine函数的t.pendown，否则判断为错误，执行函数种drawLine的t.penup
    drawLine(True) if d in [0,2,3,5,6,7,8,9] else drawLine(False)  # 这是在绘制第6段数码管，如果d在右侧列表中，则判断为正确，运行drawLine函数的t.pendown，否则判断为错误，执行函数种drawLine的t.penup
    drawLine(True) if d in [0,1,2,3,4,7,8,9] else drawLine(False)  # 这是在绘制第7段数码管，如果d在右侧列表中，则判断为正确，运行drawLine函数的t.pendown，否则判断为错误，执行函数种drawLine的t.penup
    t.left(180)  #左转180度
    t.penup()  #提起画笔
    t.fd(20)  # 前进20像素
def drawDate(date):  # 定义函数，并执行下面的函数操作
    t.pencolor('red')  # 画笔颜色为红色
    for i in date:  # 遍历参数date，这个date即是后面main函数中drawDate右边括号中的系统时间
        drawDigit(eval(i))  # 执行前面的drawDigit函数绘制七段数码管，参数是将系统时间的字符串转化后的数字
def main():  # 定义函数main，这里不需要参数，所以留空
    t.setup(800,350,200,200)  # 制作一个大小800*350的，坐标在电脑屏幕x200,y200位置的画布
    t.penup()  # 提起海龟画笔
    t.fd(-300)  # 向左移动300像素
    t.pensize(5)  # 笔触为5像素
    drawDate(time.strftime('%Y%m%d',time.gmtime()))  # 提取当前系统时间，并通过strftime函数将之转化为字符串
    t.done()  # 保持画布
main()  # 运行main函数，因为前面都是函数，没有这个，前面的函数都是不会运行的

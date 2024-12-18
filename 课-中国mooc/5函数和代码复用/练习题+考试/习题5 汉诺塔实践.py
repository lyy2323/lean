steps = 0  # 设置变量，赋值0给steps
def hanoi(src, des, mid, n):  # 定义函数hanoi，其中前面src、des和mid分别代表三个柱子，n为数字
    global steps  # 将steps变量全局化
    if n == 1:  # 如果n等于1
        steps += 1  # steps等于0+1，这里用来表示运行的步数
        print('[STEP{:>4}] {}->{}'.format(steps, src, des, mid))  # 打印结果，因为是steps=0+1，所以显示的结果是[STEP   1] A->C
    else:  # 如果n不等于1
        hanoi(src,mid,des,n-1)  # 运行函数，假设n=3，就是3-1=2，这里就是将2个圆盘从src移动到mid，des作为辅助
        steps += 1  # steps等于n+1，这里用来表示运行的步数，每运行一次增加一步
        print('[STEP{:>4}] {}->{}'.format(steps, src, des))  # 打印步数，将
        hanoi(mid,des,src,n-1)  # 这段代码也不理解，存在的意义，请解释一下
N = eval(input())  # 用户输入的字符串数值化，并赋值给N
hanoi('A','C','B',N)  # 运行函数hanoi

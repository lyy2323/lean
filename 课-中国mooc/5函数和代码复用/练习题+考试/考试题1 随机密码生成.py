import random  # 调用random库

def genpwd(length):  # 定义函数
    a = 10**(length-1)
    b = 10**length - 1
    return "{}".format(random.randint(a, b))

length = eval(input())
random.seed(17)
for i in range(3):
    print(genpwd(length))
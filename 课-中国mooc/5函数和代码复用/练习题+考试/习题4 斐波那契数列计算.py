def fbi(n):  # 定义函数
    if n == 1 or n == 2:  # 如果n是1或者2
        return 1  # 返回1
    else:  # 否则
        return fbi(n-1)+fbi(n-2)  # 返回这个公式
n = eval(input())  # n等于用户输入的数字
print(fbi(n))  #打印这个函数

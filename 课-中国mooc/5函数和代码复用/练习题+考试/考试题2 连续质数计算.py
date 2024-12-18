def prime(m):  # 定义函数
    for i in range(2,m):  # 遍历2到m（不含m），用i表示这个遍历
        if m % i == 0:  # 如果m的i模等于0
            return False  # 则返回为错误
    return True  # 其他为正确

n = eval(input())  # 将用户输入的字符串转化为数值，并赋值给n
n_ = int(n)  # 将n转为整数，并赋值给n_。有个问题：为什么上一步不直接用“n=int(input())"?
n_ = n_+1 if n_ < n else n_  # 这里不明白，请解析
count = 5

while count > 0:
    if prime(n_):
        if count > 1:
            print(n_, end=',')
        else:
             print(n_, end='')
        count -= 1
    n_ += 1

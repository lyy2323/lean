#  递归对于数字的计算
def fact(n):
    if n == 0:
        return 1
    else:
        return n*fact(n-1)
print(fact(5))

#  递归对于字符串的反转：
def rvs(s):
    if s == '':
        return s
    else:
        return rvs(s[1:])+s[0]
a = rvs('123456')
print(a)

#  递归对于斐波拉契数列的计算：
def f(n):
    if n == 1 or n == 2:
        return 1
    else:
        return f(n-1) + f(n-2)
a = f(10)
print(a)

#  汉诺塔圆盘搬运：
count = 0
def hanoi(n, src, dst, mid):
    global count
    if n == 1:
        print('{}:{}->{}'.format(1, src, dst))
        count += 1
    else:
        hanoi(n-1, src, mid, dst)
        print('{}:{}->{}'.format(n,src,dst))
        count += 1
        hanoi(n-1, mid, dst, src)
hanoi(3, 'A', 'C' ,'B')
print(count)

def fact(n, *b):
    s = 1
    for i in range(1, n+1):
        s += i
    for itu in b:
        s += itu
    return s
a = fact(2, 10,20)
print(a)

# 返回值的调整修改：
def fact(n, *b):
    s = 1
    for i in range(1, n+1):
        s += i
    for itu in b:
        s +=itu
    return s, n, b
a = fact(2,10,20)
print(a)
a, b, c = fact(2, 10,20)
print(a, b ,c)

#  全局变量与局部变量
#  规则1：全局变量与局部变量是不同的变量：
n, s = 10, 10001
def fact(n):
    s = 1  # 这里的s及上面函数中的参数n，都是局部变量，而不是外面的全局变量，如果想要将这个s改为全局变量，要在这个"s=1"改为"global s"，这时这个s就是上面的10001
    for i in range(1, n+1):
        s += i
    return s
a = fact(4)
print(a, s)  # 这里的s，是函数外面的s，即全局变量，而不是函数里面的局部变量s

#  规则2：局部变量为组合类型并且未被创建，则等同于全局变量：
Is = ['f', 'F']
def fact(n):
    Is = ['D', 'R']  # 变量遮蔽
    Is.append(n)
    return Is
print(fact('c'))
print(Is)

#  lambda函数的说明：
f = lambda x, y : x + y
f = (10, 15)
print(f)
def cmul(a, *b):  # 定义函数cmul，这里的参数我只知道a要是个数字，*b是可以多个数字，请问这样也是递归函数吗？
    m = a
    for i in b:  # 遍历b，后面用i表示
        m *= i  # m等于m乘以i
    return m  # 返回为m
print(eval('cmul({})'.format(input())))  # 这里不太懂，"cmul({})"这个用引号引起来的不是字符擦吗？为什么还被认为是函数？
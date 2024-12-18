import ast

def getNum():  # 获取用户不定长度的输入
    s = input()
    try:
        ls = list(ast.literal_eval(s))
        return ls
    except ValueError:
        print("输入有误，请重新输入。")
        return getNum()

def mean(numbers):  # 计算平均值
    s = 0.0
    for num in numbers:
        s = s + num
    return s / len(numbers)

def dev(numbers, mean):  # 计算标准差
    sdev = 0.0
    for num in numbers:
        sdev = sdev + (num - mean)**2
    return pow(sdev / (len(numbers)-1), 0.5)

def median(numbers):  # 计算中位数
    numbers.sort()
    size = len(numbers)
    if size % 2 == 0:
        med = (numbers[size//2-1] + numbers[size//2])/2
    else:
        med = numbers[size//2]
    return med

n = getNum()  # 主体函数
m = mean(n)
std_dev = dev(n, m)
print('平均值:{:.2f},标准差:{:.2f},中位数:{}'.format(m, std_dev, median(n)))
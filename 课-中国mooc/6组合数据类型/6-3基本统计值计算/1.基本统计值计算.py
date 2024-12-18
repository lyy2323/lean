def getNum():  # 获取用户不定长度的输入函数
    nums = []
    iNumstr = input('请输入数字（回车退出）：')
    while iNumstr != '':
        nums.append(eval(iNumstr))
        iNumstr = input('请输入数字（回车退出）：')
    return nums

def mean(numbers):  # 计算平均值的函数
    s = 0.0
    for num in numbers:
        s = s + num
    return s / len(numbers)
# 上面的这个mean函数，也有更简便的函数如下：
''' 
def mean(numbers):
    if not numbers: # 这里是检查列表是否为空，空则返回为0
        return 0
    return sum(numbers) / len(numbers)
print(mean[1,2,3,4,5])
# 这个函数和上面的效果是一样的
'''

def dev(numbers,mean):  # 计算方差的函数
    sdev = 0.0
    for num in numbers:
        sdev = sdev + (num - mean)**2
    return pow(sdev / (len(numbers)-1),0.5)

def median(numbers):  # 计算中位数的函数
    sorted(numbers)
    size = len(numbers)
    if size % 2 == 0:
        med = (numbers[size//2-1] + numbers[size//2])/2
    else:
        med = numbers[size//2]
    return med

print(getNum())
print(mean([1,2,3,4,5]))

n = getNum()
m = mean(n)
print('平均值:{},方差：{:.2},中位数：{}.'.format(m,dev(n,m),median(n)))

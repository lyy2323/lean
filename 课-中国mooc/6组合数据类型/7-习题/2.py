def getNum():  # 获取用户不定长度的输入
    s = input("请输入数字列表（用逗号分隔，如1,2,3）：")
    try:
        # 安全处理输入，将输入字符串拆分为列表，过滤掉非数字字符
        ls = list(map(float, s.split(',')))
    except ValueError:
        print("输入错误，请输入有效的数字列表")
        return []
    return ls

def mean(numbers):  # 计算平均值
    s = 0.0
    for num in numbers:
        s += num
    return s / len(numbers) if len(numbers) > 0 else 0

def dev(numbers, mean):  # 计算标准差
    sdev = 0.0
    for num in numbers:
        sdev += (num - mean) ** 2
    return pow(sdev / (len(numbers) - 1), 0.5) if len(numbers) > 1 else 0

def median(numbers):  # 计算中位数
    sorted_numbers = sorted(numbers)
    size = len(sorted_numbers)
    if size % 2 == 0:
        med = (sorted_numbers[size // 2 - 1] + sorted_numbers[size // 2]) / 2
    else:
        med = sorted_numbers[size // 2]
    return med

n = getNum()  # 主体函数
if n:  # 检查是否获得了有效输入
    m = mean(n)
    sd = dev(n, m)
    med = median(n)
    print('平均值: {:.2f}, 标准差: {:.2f}, 中位数: {}'.format(m, sd, med))
def dayUP(df):  # 定义dayUP和参数df
    dayup = 1  # 1赋值给dayup
    for i in range(365):  # 循环范围365
        if i % 7 in [6,0]:  # 如果7的模运算结果是6或为0时
            dayup = dayup*(1 - 0.01)  # 计算结果
        else:  # 其他
            dayup = dayup*(1 + df)  # 计算结果
    return dayup  # 返回dayup
dayfactor = 0.01  # ???这里为什么会出现这个？
while dayUP(dayfactor) < 37.78:  # 循环前面定义的函数dayUP，如果小于37.78，则继续按下面的要求（参数增加0.001）前面循环，如果大于等于则停止：
    dayfactor += 0.001  # 参数增加0.001，并继续前面循环
print('工作日的努力参数是：{:.3f}'.format(dayfactor))  # 打印结果，保留3个浮点数
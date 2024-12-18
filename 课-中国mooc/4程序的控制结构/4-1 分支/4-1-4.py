#  异常处理语句：
try:  # 尝试做什么，比如尝试输入。。。
    print(eval(input('请输入数字：')))
except:  # 错误的时候出现，可以理解为except（除了）上面的以外，会出现。。。
    print('输入有误')
else:  # 正确的时候出现，可以理解为上面except的else（其他的），因为它不能在except不在的时候出现。
    print('正确')
finally:  # 无论正确与否，都会出现的反馈
    print('很zhengque')
# 时间库：
import time
print(time.time())  # 获取计算机当前时间，以浮点数的形式显示
print(time.ctime())  # 获取计算机当前时间，以人类语言看得懂的语言显示
print(time.gmtime())  # 获取计算机当前时间，以计算机可处理的格式显示

t = time.gmtime()  # 将time.gmtime()赋值给t
print(time.strftime('%Y-%m-%d %H:%M:%S',t))  # 按指定的时间格式打印

timestr = '2024-07-21 09:19:30'
print(time.strptime(timestr,'%Y-%m-%d %H:%M:%S'))

# 程序计时：
start = time.perf_counter()
def wait():
    time.sleep(0.2)
wait()
end = time.perf_counter()
print(start,end)
print(end - start)

# 文本进度条：
import time
scale = 10
print('-----执行开始-----')
for i in range(scale+1):
    a = '*' * i
    b = '.' * (scale-i)
    c = (i/scale)*100
    print('{:>3.0f}%[{}->{}]'.format(c,a,b)) # 格式化为浮点数，右对齐，占3个字符宽度，保留0位小数。{}是占位符，用于插入变量a和b
    time.sleep(0.1)
print('-----执行结束-----')

import time
for i in range(101):
    print('\r{:2}%'.format(i),end='')
    time.sleep(0.01)

print()

import time
scale = 50  # 长度位50字符（即后面的“*”）
print('执行时间'.center(scale//2,'-'))  # 将“执行时间”居中打印在50/2=25的宽度中，其他部分用“-”表示
start = time.perf_counter()  # 获取开始时的计算机时间
for i in range(scale+1):  # 循环i,即循环从0~50，每次+1
    a = '*' * i  # *乘以i
    b = '.' * (scale - i)  # “.”乘以（i-1）
    c = (i/scale)*100  # （当前的i-50）*100=进度%
    dur = time.perf_counter() - start  # 用当前计算机时间减去前面开始的时间（start）
    print('\r{:>3.0f}%[{}->{}]{:.2f}s'.format(c,a,b,dur),end='')  # 三个占位槽：c（光标移到前面、右对齐、3个字符宽、0浮点）、%、a+b占位槽、dur占位槽2个浮点、s
    time.sleep(0.01)  # 从0~50，每次0.01秒
print('\n'+'执行结束'.center(scale//2,'-'))
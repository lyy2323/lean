"""
数据类型包括：
1、字符串、数字
2、列表、字典、元组、集合
"""

"""1~~~~~"""
# 变量
x = 10
print(x) # 返回：10
y = x + 15
print(y) # 返回：25

# 查询数据类型
name = "Tom"
number = "88"
number1 = 99
number2 = 55.2
print(type(name)) # <class 'str'>
print(type(number)) # <class 'str'>
print(type(number1)) # <class 'int'>
print(type(number2)) # <class 'float'>

# 数据转换为字符串
a = 88
b = str(a)
print(type(a)) # <class 'int'>
print(type(b)) # <class 'str'>

# 字符串转换为数字
a = "88"
b = int(a)
print(type(a)) # <class 'str'>
print(type(b)) # <class 'int'>

# 浮点数与数字互转
a = 5.8
b = (int(a))
c = 5
d = (float(c))
print(type(a)) # <class 'float'>
print(type(b)) # <class 'int'>
print(type(c)) # <class 'int'>
print(type(d)) # <class 'float'>

"""2~~~~~"""
# 列表中可以包含字符串、数字、甚至包含列表
class1 = ["123", 2, "字符串", [1, 2, 3]] #通过for循环可以逐个打印出来
for i in class1:
    print(i)
# 返回：
# 123
# 2
# 字符串
# [1, 2, 3]

print(len(class1)) # 返回：4
print(class1[2]) # 返回：字符串
print(class1[1:3]) # 返回：[2, '字符串']
print(class1[:3]) # 返回：['123', 2, '字符串']
print(class1[:-1]) # 返回：['123', 2, '字符串']

# 列表中添加元素
score = [] # 创建一个空列表
score.append(80+2) # 在空列表中添加元素（数字80）
print(score) # 返回：[82]
score.append(90) # 再增加一个元素
score.append("字符串") # 再增加一个元素——字符串
score.append([6, 5, 4]) # 再增加一个元素——列表
print(score) # 返回：[82, 90, '字符串', [6, 5, 4]]

# 用join()函数，将列表转换为字符串：
line = ["丁一", "王二", "张三", "李四", "赵五"]
new_line = ",".join(line) # 变量名 = 连接符.join(列表名)
print(new_line) # 返回：丁一,王二,张三,李四,赵五
# 如果列表中包含了非字符串，需要再join函数中使用map函数，将其转为字符串后打印
new_score = ",".join(map(str, score))
print(new_score) # 返回：82,90,字符串,[6, 5, 4]

# 用split()函数，将字符串拆分
line = ("你好,shang,hai")
print(line.split(",")) # 去掉“，”，返回为三个字符串，如果将“，”替换为其他如“s”效果类似

# 字典：是键值对，用大括号表示——{}，键相当于钥匙，值相当于是锁
class1 = {"丁一": 85, "王二": 95, "张三": 75, "李四": 65, "赵五": 55}
score = class1["张三"] # 提取值的时，这里输入的是键，相当于要打开这把锁，这里输入的是钥匙
print(score) # 返回：75
for k, i in class1.items(): # 用for循环时，如果range是键值对（即.items）时，前面i的前面需要加上"k,i"相当于也要
    print(f"这里显示的是键:{k},和值:{i}")
for i in class1.keys(): # 而如果后面的range部分已经著名keys（即键），或.values（剑值）的话，则前面i部分只要一个i就可以了
    print(f"这里只显示键：{i}")

"""
元组的定义与使用方法与列表非常类似，
区别在于：
1、列表用的是中括号[],元组用的是小括号()
2、元组不可修改
"""
a = ("丁一", "王二", "张三", "李四", "赵五")
print(a[1:3]) # ('王二', '张三')
print(len(a[1:3])) # 返回：2

"""
集合是一个无需的不重复序列————集合中不会有重复的元素
可以使用大括号{}来定义集合，也可以使用set()函数来创建集合
"""
a = ["丁一", "王二", "张三", "李四", "赵五"]
print(set(a)) # 返回集合：{'李四', '王二', '赵五', '丁一', '张三'}
a = {'李四', '王二', '赵五', '丁一', '张三'}
print(a) # {'张三', '王二', '李四', '赵五', '丁一'}

"""
运算符：
加减乘除：+-*/
幂：**
整除（舍弃小数部分，不做四舍五入）：//
取模（计算两个正整数相除后的余数：%
"""
# 以上，+和*除了用于数字，也可以用在字符串，如：
a = "hello"
b = "world"
c = a + " " + b # 中间双引号为的是留空格
print(c) # hello world
print(a * 3) # hellohellohello

"""
比较运算符：
大于：>，小于:<, 大于等于：>=，小于等于：<=，判断两侧相等：==，不等于：!=

赋值运算符：
右侧赋值给左侧：=
执行加法（即减\乘\除\幂\整除\模）后的结果赋值给左侧：+=、-=、*=、/=、**=、//=、%=

逻辑运算符：
左右两侧的关系是（与、或、非）为True时返回True，否则返回False
"""

"""2.6 控制语句：for、while"""

for i in range(3):  # range()就是数字，其中是0~2（不含2）
    print("第", i + 2, "次")  # 第一次遍历的i=0，第二次=1，第三次=2，所以这里返回第2、3、4次

"""
while的两种形式：
    while （条件）：
        执行代码
    while （True）：
        执行代码
"""
# 控制语句可以互相嵌套使用，
# if中嵌套if：：
math = 95
chinese = 80
if math >=90:
    if chinese >=90:
        print("优秀")
    else:
        print("加油！")
else:
    print("继续加油")
# for中嵌套if：
for i in range(3):
    if i == 1:
        print("加油")
    else:
        print("安静")

"""
我的理解：函数分为内置函数和方法（函数）
此部分是函数：分为内置函数，和自定义函数，"print()"就是内置函数，而“def..."则是自定义函数
"""
# len():是length（词义：长度）的缩写，用于统计列表元素个数的函数
line = [1, 2, 3, 1, 2, 3]
print(len(line))  # 返回：6

"""
我的理解：方法类函数，一般的语法格式与内置函数不同，是：字符串.方法函数()
"""
# replace():词义是“代替、放回原处”的意思，用于在字符串中查找和替换
# 方法类函数，语法格式：字符串.replace（要查找的内容, 要替换的内容）
a = "继续加油！"
a = a.replace("继续", "就要")
print(a)  # 返回：就要加油！

# strip():词义是“剥去”的意思，用于删除字符串两端的空白符（包括换行符和空格），如要剥去左边则改为lstrip，右边则改为rstrip
# 方法类函数，语法格式：字符串.strip()
a = "   学而时习之，不亦说乎！\n"
print(a)
a = a.strip("，")
print(a)

# split():词义是”分开“，用于将指定字符串拆分为一个列表：
today = "2025-02-15"
a = today.split("-")  # 括号中间的字符串是要split的位置，并用删除
print(a)

"""
自定义函数，语法格式：
    def 函数名（形参）：
        代码块


导入函数或第三方模块的几种方法：
import 模块名
import 模块名 as 别名

import 模块名 import *
（这样的方法好处是调用该模块函数时，不需要在函数的前面加上“.模块名”

from 模块名 import 函数名
（如有多个”函数名“可以用英文逗号隔开，这样不仅避免模块太大导致运行变慢或打包太大实际使用中也不需要输入模块名）
from 模块名 import 函数名 as 函数的别名
"""
import math  # 第一种方法
a = math.sqrt(16)  # 使用时：”模块名.函数名（）“
from math import *
b = sqrt(16)
from math import sqrt
c = sqrt(16)  # 这个的使用，仅输入”函数名（）“即可


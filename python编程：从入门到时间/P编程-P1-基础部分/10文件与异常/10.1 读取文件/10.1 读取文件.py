from pathlib import Path
from traceback import print_list

# 10.1 读取文件
# 创建一个路径对象
path = Path("pi_digits.txt")
contents = path.read_text().rstrip()
# 打印路径
print(contents)

path = Path("pi_digits.txt")
contents = path.read_text()

for line in contents.splitlines():
    print(f"第一行：{line}")

# 10.1.1 读取文件的全部内容
from pathlib import Path

path = Path("pi_digits.txt")
contents = path.read_text()

pi_string = ""
for line in contents.splitlines():
    print(f"按行返回列表：{line}")
    pi_string += line.lstrip()  # 删除文件中（可见的）每行左侧的空格
print(f"这个字符串是一个整体：{pi_string}")
print(float(pi_string))  # 所有文本提取出来的数字都是字符串，要将字符串改为数字需要用int或float
print(len(pi_string))  # 字符串的长度


# 10.1.5 包含100万位的大型文件
from pathlib import Path

path = Path("pi_million_digits.txt")
contents = path.read_text()

pi_string = ""
for line in contents.splitlines():
    pi_string += line.lstrip()

print(f"打印到小数点后50位：{pi_string[:52]}...")
print(len(pi_string))

# 10.1.6 圆周率中包含你的生日吗
from pathlib import Path
path = Path("pi_million_digits.txt")
contents = path.read_text()

pi_string = ""
for line in contents.splitlines():
    pi_string += line.lstrip()
birthday = input("这里输入生日可以查询是否在圆周率中：")
if birthday in pi_string:
    print("在呢！")
else:
    print("不在~")
from pathlib import Path

path = Path("programming.txt")

grest_names = []

while True:
    name = input("请输入姓名（如果输入”quit“则退出）：")
    if name == "quit":
        print("程序已退出~")
        break
    print(f"谢谢{name}加入！")

    grest_names.append(name)

# 创建一个字符串，他们包含所有的名字，且在每个名字后面都换行
file_string = ""
for name in grest_names:
    file_string += f"{name}\n"


path.write_text(file_string, encoding="utf-8")
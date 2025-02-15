from pathlib import Path
import json


# 用json.dumps()将内容加载到python文件中
numbers  = [1, 3, 5, 7, 11, 13]

path = Path("number.json")
contents = json.dumps(numbers)
path.write_text(contents)

# 用json.loads()加载文件内容
path = Path("number.json")
contents = path.read_text()
numbers = json.loads(contents)
print(numbers)

# 让用户输入文字到json中
username = input("请输入你的名字或其他信息：")

path = Path("username.json")
contents = json.dumps(username, ensure_ascii=False)
path.write_text(contents, encoding="utf-8")
print(f"你的输入是{username}!")
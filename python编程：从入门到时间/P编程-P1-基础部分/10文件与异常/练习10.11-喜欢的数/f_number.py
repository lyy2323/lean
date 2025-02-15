from pathlib import Path
import json

number = input("请输入你喜欢的数字：")

path = Path("number_f.json")
contents = json.dumps(number)
path.write_text(contents)
print("谢谢，我们会记住这个的！")

path = Path("number_f.json")
contents = path.read_text()
number = json.loads(contents)

print(f"我知道你最喜欢的数字是{number}")

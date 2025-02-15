from pathlib import Path
import json

path = Path("number_f.json")

number = input("请输入你喜欢的数字：")
if number:
    print(f"已经存在：{number}")
else:
    input("数字不存在，请输入：")
    path = Path("number_f.json")
    contents = json.dumps(number)
    path.write_text(contents)
    print("谢谢，我们会记住这个的！")

    path = Path("number_f.json")
    contents = path.read_text()
    number = json.loads(contents)


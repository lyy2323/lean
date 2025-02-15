from pathlib import Path
import json

path = Path("username.json")
if path.exists():
    contents = path.read_text()
    username = json.loads(contents)
    print(f"欢迎回来{username}")
else:
    username = input("你的名字是？")
    contents = json.dumps(username)
    path.write_text(contents)
    print(f"欢迎{username}，我们下次会记得你的{username}")

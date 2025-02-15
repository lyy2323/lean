from pathlib import Path
path = Path("programming.txt")
try:
    contents = path.read_text(encoding="utf-8")
except FileNotFoundError:
    print(f"对不起，'{path}'不存在！")
else:
    words = contents.split()
    num_words = len(words)
    print(f"这个文件{path}，它的文字有{num_words}个！")
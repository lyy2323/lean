# 10.8 猫和狗
from pathlib import Path
try:
    path = Path("cats.txt")
    cont = path.read_text(encoding="utf-8")
    print(cont)
except FileNotFoundError:
    print("文件路径不存在")

# 练习10.9 静默的猫和狗
try:
    path = Path("cat.txt")
    cont = path.read_text(encoding="utf-8")
    print(cont)
except FileNotFoundError:
    pass

print("运行结束")
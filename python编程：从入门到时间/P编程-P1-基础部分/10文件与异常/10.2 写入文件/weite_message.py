from pathlib import Path

path = Path("programming.txt")
path.write_text("新写入的内容~~~", encoding="utf-8")

w_txt = input("请在这里输入内容：")
path.write_text(w_txt, encoding="utf-8")
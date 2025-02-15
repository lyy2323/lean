from pathlib import Path
path = Path("learning_python.txt")
look_txt = path.read_text(encoding='UTF-8')
print(look_txt)

def l_txt():
    lok_txt = look_txt.splitlines()
    for i in lok_txt:
        print(f"11{i}")
l_txt()

r_look_txt = look_txt.replace("python", "C++")
print(r_look_txt)

print(look_txt)
from pathlib import Path

def count_txt(file, words):
    path = Path(file)
    contents = path.read_text(encoding="utf-8")
    word_count = contents.lower().count(words)
    print(f"{words}在{file}中出现的次数是{word_count}次")

filename = "cats.txt"
count_txt(filename, "the ")
count_txt(filename, "喵")
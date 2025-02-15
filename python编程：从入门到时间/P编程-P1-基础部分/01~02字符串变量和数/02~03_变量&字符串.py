first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(full_name)
print(full_name.title())
print(f"Hello,{full_name.title()}!")

# 也可以将类似上面的整条消息赋值给变量：
message = f"Hello,{full_name.title()}!"
print(message)
#  当然，修改“方法”，也同样能将其格式全部改为大写：
message = f"Hello,{full_name.upper()}!"
print(message)

# 使用制表符（\t）、换行符（\n）、来添加空白：
print("python")
print("\tpython")
print("Languages:\n\tpython\n\tC\n\tJavaScript")

# 使用删除空白的方法代码strip（左侧lstrip、右侧rstrip，而如果是strip则是删除两侧的空白）：
favorite_language = ' python'
print(favorite_language)
print(favorite_language.lstrip())
# 上面的方法只是删除这个空格，要永久删除，需要如下通过变量删除：
favorite_language = favorite_language.lstrip()
print(favorite_language)

# 使用（左侧removeprefix、右侧removesuffix）方法代码删除前缀
nostarch_url = "https://nostarch.com"
new_nostarch_url = nostarch_url.removeprefix("https://")
print(new_nostarch_url)
# 和前面一样，如果希望永久删除前缀，也可以复制给变量
simple_url = nostarch_url.removeprefix('https://')
print(simple_url)

# 右侧removesuffix
t = "python.txt"
print(t)
new_t = t.removesuffix(".txt")
print(new_t)

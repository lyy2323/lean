
def greet_user(name):
    print(f"111,{name.title()}")
greet_user("aaaa")
greet_user("ddd")
greet_user("cccc")

def display_message():
    print(f"这是函数中的打印")
display_message()

def favorite_book(title,ti="111"):
    print(f"{ti}One of my favorite books {title.title()}")
favorite_book(title="《fox and flor》")
favorite_book(ti="222", title="dddd")
favorite_book()
promd = "请说出你想要的披萨"
promd += "\n如果实在没有，请输入‘quit’"
"""
while True:
    topping = input(promd)
    if topping != "quit":
        print(f"你喜欢的是{topping}")
    else:
        break
"""
active = True
while active:
    topping = input(promd)

    if topping == "quit":
        active = False
    else:
        print(f"你喜欢的是{topping}")

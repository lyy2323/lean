"""
pizza = ""
while pizza != "quit":
    pizza = input("please speak you like pizza")
    print(f"you like pizza is {pizza}")
"""

# 正确答案

promd = "请说出你想要的披萨"
promd += "\n如果实在没有，请输入‘quit’"

while True:
    topping = input(promd)
    if topping != "quit":
        print(f"你喜欢的是{topping}")
    else:
        break

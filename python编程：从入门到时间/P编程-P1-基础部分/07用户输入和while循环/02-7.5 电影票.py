"""
moves = "请输入你的年龄"
moves += "我们会根据你的年龄来提供不同优惠"

while True:
    move = input(int(moves))
    if move < 3:
        print("免费")
    elif move < 12:
        print("10美元")
    elif move < 15:
        print("15美元")
    else:
        break
"""

# 正确答案：
moves = "请输入你的年龄"
moves += "\n我们会根据你的年龄来提供不同优惠"
while True:
    age = input(moves)
    if age == "quit":
        break
    age = int(age)
    if age < 3 :
        print("免费")
    elif age < 12 :
        print("10")
    else :
        print("15")
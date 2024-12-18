print("猜数字游戏")
while True:
    num = input("请输入数字：")
    new_num = num.upper()
    if new_num == "Q":
        break

    if num == "100":
        print("恭喜你，中奖啦！")
        break
    else:
        print("很遗憾(:")

import random

# 定义手势列表
gestures = ["石头", "剪刀", "布"]

# 获取用户的选择
user_choice = input("请输入你的选择（石头/剪刀/布）：")

# 检查用户输入是否合法
if user_choice not in gestures:
    print("输入错误，请重新输入。")
else:
    # 生成电脑的随机选择
    computer_choice = random.choice(gestures)

    # 打印双方的选择
    print(f"你选择了：{user_choice}")
    print(f"电脑选择了：{computer_choice}")

    # 判断胜负
    if user_choice == computer_choice:
        print("平局！")
    elif (user_choice == "石头" and computer_choice == "剪刀") or (user_choice == "剪刀" and computer_choice == "布") or (user_choice == "布" and computer_choice == "石头"):
        print("你赢了！")
    else:
        print("你输了！")
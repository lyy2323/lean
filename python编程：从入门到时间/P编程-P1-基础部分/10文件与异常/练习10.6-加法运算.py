while True:

    try:
        x = input("请输入一个数字：")
        x = int(x)
        y = input("请再输入一个数字：")
        y = int(y)

    except ValueError:
        print("请输入数字！")

    else:
        sum = x+y
        print(sum)
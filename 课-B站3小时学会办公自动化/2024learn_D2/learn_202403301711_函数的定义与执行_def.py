# 第一段
def send_email():
    print("发送邮件")


# 第一段的执行函数
send_email()
# 第二段


def send_email(to):
    message = "给" + to + "发送邮件"
    print(message)


# 第二段的执行函数
send_email("刘邦")
send_email("pepsi")


while True:
    name = input("请输入姓名：")
    send_email(name)
    if name == "w":
        break


# 第三段代码
def plus(a1, a2):
    number = a1 + a2
    print(number)


plus(100, 200)
plus(300, 222)

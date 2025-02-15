# 8.9 消息
def show_massages(massages):
    for massage in massages:
        mag = f"Hello,{massage.title()}"
        print(mag)
m = ["adfasf", "fadaf", "aeqrqe"]
show_massages(m)

print()

# 8.10 发送消息

def send_massages(send, sent):
    while send:
        send_m = send.pop()
        print(f"打印了{send_m}")
        sent.append(send_m)

def show_massages(sent):
    print(f"转过来了：")
    for i in sent:
        print(i)


send = ["asfda", "3423", "sfaf"]
sent = []
send_massages(send, sent)
show_massages(sent)

print("\n以下是8.11\n")
# 8.11 归档消息（在上段的基础上，增加一个切片即可）

def send_massages(send, sent):
    while send:
        send_m = send.pop()
        print(f"打印了{send_m}")
        sent.append(send_m)

def show_massages(sent):
    print(f"转过来了：")
    for i in sent:
        print(i)


send = ["asfda", "3423", "sfaf"]
sent = []
send_massages(send[:], sent)
show_massages(sent)

print("原始的send:")
print(send)
print("调用后的sent:")
print(sent)

print()

# 8.12-三明治
def sandwichs(*names):
    print("这里有这些三明治：")
    for name in names:
        print(f"-{name}")
sandwichs("adsfa", "adfasf", "asdfadfd")
sandwichs("sdfadf")

# 8.13-用户简介：
def build_profile(frist, list, **user_info):
    user_info["frist_name"] = frist
    user_info["list_name"] = list
    return user_info
mybuild = build_profile("xuefeng", "liu", hobby="羽毛球", occupation="职员")
print(mybuild)

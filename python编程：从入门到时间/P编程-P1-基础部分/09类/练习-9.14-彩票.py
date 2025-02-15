#  练习9.14 彩票：
from random import choice
caipiao = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd', 'e']
winning_ticket = []
print("让我们看看什么结果吧！")
#  中将组合中不能包含重复的数据或字母，因此使用了while循环
while len(winning_ticket) < 4:
    pulled_item = choice(caipiao)
    #  仅当摇出的数字或字母不在组合中时，才将其添加到组合中
    if pulled_item not in winning_ticket:
        print(f"本次结果是：{pulled_item}")
        winning_ticket.append(pulled_item)
print(f"\n本次全部四个双色球是：{winning_ticket}")
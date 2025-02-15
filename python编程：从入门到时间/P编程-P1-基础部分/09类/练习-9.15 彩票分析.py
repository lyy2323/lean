from random import choice

def get_winning_ticket(possibilities):
    """摇出中将组合"""
    winning_ticket = []

    # 中奖组合中不能包含重复的数字或字母，因此使用了while循环
    while len(winning_ticket) < 4:
        pulled_item = choice(possibilities)

        if pulled_item not in winning_ticket:
            winning_ticket.append(pulled_item)
    return winning_ticket

def check_ticket(played_ticket, winning_ticket):
    # 检查彩票的每个数字或字母，只要有一个不在中将组合中，就返回False
    for element in played_ticket:
        if element not in winning_ticket:
            return False
        # 如果代码执行到这里，就说明中将了
    return True

def make_random_ticket(possibilities):
    """随机地生成彩票"""
    ticket = []
    # 彩票不能包含重复的数字或字母，因此使用了while循环
    while len(ticket) < 4:
        pulled_item = choice(possibilities)
        # 只有当随机生成的数字或字母不在彩票中时，才将其添加到彩票中
        if pulled_item not in ticket:
            ticket.append(pulled_item)
    return  ticket

possibilities = [1, 2, 3, 4, 5, "a", "b", "c", "d", "e"]
winning_ticket = get_winning_ticket((possibilities))

print(f"中将组合是：{winning_ticket}")

plays = 0
won = False

# 为避免程序执行时间太长，设置最多随机生成多少张彩票
max_tries = 15_000

while not won:
    new_ticket = make_random_ticket(possibilities)
    won = check_ticket(new_ticket,winning_ticket)
    plays += 1
    if plays >= max_tries:
        break

    if won:
        print("我们中奖一张彩票")
        print(f"你的彩票是：{new_ticket}")
        print(f"中将的彩票：{winning_ticket}")
        print(f"他进行了{plays}次中奖的！")
    else:
        print(f"很遗憾，{plays}次，没有中奖")
        print(f"你的彩票：{new_ticket}")
        print(f"中奖彩票：{winning_ticket}")





# 可重复
from random import choice

def get_winning_ticket(possibilities):
    """摇出中将组合"""
    winning_ticket = []

    # 中奖组合中不能包含重复的数字或字母，因此使用了while循环
    while len(winning_ticket) < 10:
        pulled_item = choice(possibilities)
        winning_ticket.append(pulled_item)
    return winning_ticket

def check_ticket(played_ticket, winning_ticket):
    # 检查彩票的每个数字或字母，只要有一个不在中将组合中，就返回False
    for element in played_ticket:
        if element not in winning_ticket:
            return False
        # 如果代码执行到这里，就说明中将了
    return True

def make_random_ticket(possibilities):
    """随机地生成彩票"""
    ticket = []
    # 彩票不能包含重复的数字或字母，因此使用了while循环
    while len(ticket) < 10:
        pulled_item = choice(possibilities)
        # 只有当随机生成的数字或字母不在彩票中时，才将其添加到彩票中
        ticket.append(pulled_item)
    return  ticket

possibilities = [1, 2, 3, 4, 5, "a", "b", "c", "d", "e"]
winning_ticket = get_winning_ticket((possibilities))

print(f"中将组合是：{winning_ticket}")

plays = 0
won = False

# 为避免程序执行时间太长，设置最多随机生成多少张彩票
max_tries = 15_000

while not won:
    new_ticket = make_random_ticket(possibilities)
    won = check_ticket(new_ticket,winning_ticket)
    plays += 1
    if plays >= max_tries:
        break

    if won:
        print("我们中奖一张彩票")
        print(f"你的彩票是：{new_ticket}")
        print(f"中将的彩票：{winning_ticket}")
        print(f"他进行了{plays}次中奖的！")
    else:
        print(f"很遗憾，{plays}次，没有中奖")
        print(f"你的彩票：{new_ticket}")
        print(f"中奖彩票：{winning_ticket}")
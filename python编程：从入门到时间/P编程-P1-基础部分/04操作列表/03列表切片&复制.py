# 4.1 切片
players = ['one', 'tow', '333', '444', '555']
print(players[1:3])
print(players[:3])
print(players[-3:])
print(players[:-3])
print(players[1:5:2]) # 其中2是步长，注意切片之间是冒号，不仅位置，也包括步长之间

# 4.2 遍历切片
# 通过for循环使用切片，显示位置名称：
for number in players[1:3]:
    print(number.title())

# 4.3 复制列表
friend_player = players[:]  # 关键点注意：一定是复制列表（即players[])，而不是变量名（players）
players.append('1010')
friend_player.append('zzzz')
print(players[:])
print(friend_player[:])

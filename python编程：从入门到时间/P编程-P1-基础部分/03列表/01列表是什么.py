
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[0].title())  # 正序
print(bicycles[-4])  # 倒序

# 也可以适用f方法（format的简写）+花括号的方法更方便：
message = f"My first bicycle was a {bicycles[0].title()}."
print(message)

names = ['老炮儿', '花括号', '名爵', '好说话']
print(names[1],' 需要出现的是花括号')
print(f"名爵你好,是的{names[2]}，就是你！")

# 修改列表中的元素（举例：入游戏中的任务被消灭，替换为另一个NPC）：
# 1、替换
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles[1] = 'ducati'
print(motorcycles)
# 2、再将上面消失的honda添加在末尾：
motorcycles.append('yamaha')
print(motorcycles)

# 在空的列表中运用append()方法添加元素：
motorcycles = []
print(motorcycles)
motorcycles.append('honda')
motorcycles.append('suzuki')
motorcycles.append('yamaha')
print(motorcycles)
# 通过insert()方法，可以将元素添加在列表的任意位置：
motorcycles.insert(1,'duceti')
print(motorcycles)
# 通过del函数，可以删除任意位置的元素：
del motorcycles[1:3]  # 这里的1~3，不包含1，即其实是2~3
print(motorcycles)
del motorcycles[1]
print(motorcycles)
# 恢复到原有列表：
motorcycles.append('suzuki')
motorcycles.append('yamaha')
motorcycles.append('duceti')
print(motorcycles)
# 使用pop()方法，从列表中剔出元素，并保留元素，将该元素赋值给另一个变量：
new_motorcycles = motorcycles.pop(1) # 如果索引位置留空，则剔出列表的最后一个
print(motorcycles)
print(new_motorcycles) # 因为他已经不是列表，只是一个普通的元素，所以并不以列表形式显示
print(f"the last motorcycle I owned was a {new_motorcycles}.")

# 如果不想用位置，而想用元素名来删除，可以使用remove()方法：
motorcycles.remove('honda')
print(motorcycles)

# 恢复到原有的列表：
motorcycles.append('suzuki')
print(motorcycles)
# 通过remove()方法，也可以实现删除后继续使用该元素的效果：
too_motorcycles = 'duceti'
motorcycles.remove(too_motorcycles)
print(motorcycles)
print(f'\nA {too_motorcycles.title()} is too expensive for me.')

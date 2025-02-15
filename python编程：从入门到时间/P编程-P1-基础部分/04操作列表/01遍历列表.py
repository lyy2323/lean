magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)
    print(f"goog!{magician.title()},very good!\n")
print('thinks!')

foods = ['board', 'cake', 'rice', 'dumpling']
for food in foods:
    print(food.upper())
    print(f'I like {food.title}!\n')
print('haha')

for number in range(5):
    print(number)
# 通过list()函数将数字转换为列表：
numbers = list(range(5))
print(numbers)

squares = []
for value in range(1,11):
    square = value ** 2
    squares.append(square)
print(squares)

# 更简化的代码
squares = []
for value in range(1,11):
    squares.append(value ** 2)
print(squares)

# 更更简化的代码——列表推导式
squares = [value**2 for value in range(1,11)]
print(squares)

# 对数值列表执行简单的统计计算
digits = [1,2,3,4,5,6,7,8,9,0]
print(max(digits))
print(min(digits))
print(sum(digits))

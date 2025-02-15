alien_color = 'green'
if alien_color == 'green':
    print('you are 5')

# 这个版本将没有输出：
alien_color = 'green'
if alien_color == 'red':
    print('you are 5')

# 外星人的颜色2：if-else函数，各执行一条
# 1：
if alien_color == 'green':
    print('you are 5')
else:
    print('you are 10')
# 2：
if alien_color == 'red':
    print('you are 5')
elif alien_color == 'yellow':
    print('you are 10')
else:
    print('you are 20')

# 人生不同阶段：
age = 5
if age < 2:
    ages = '婴儿'
elif age < 4:
    ages = '幼儿'
elif age < 13:
    ages = '儿童'
elif age < 18:
    ages = '少年'
elif age < 65:
    ages = '中青年人'
else:
    ages = '老年人'
print(f'你当前的年龄阶段是{ages}')

fruit = ['apple', 'orange', 'pineapple', 'banana']
if 'apple' in fruit:
    print('You really like apple')
if 'watermelon' in fruit:
    print('You really like watermelon')
if 'banana' in fruit:
    print('You really like banana')
if 'watermelon' not in fruit:
    print('haha')
# 元组与列表的两个主要区别：1、元组不能被修改，列表可以；2、元组使用圆括号，列表使用方括号
# 建立5个元组，用for循环打印
restaurant = ('rice', 'noodle' 'pasta', 'pizza', 'pineapple')
for food in restaurant:
    print(food)
# 尝试修改元组（下面的代码是列表，如果将其改为元组形式，即第一行的方括号改为圆括号，即报错）：
restaurants = ["111", '111114', '113232']
restaurants[2] = '2111'
print(restaurants)

# 更换第一行的元组内容，然后用for循环打印第一段的元组
restaurant = ('rice', 'noodle', 'dumpling', 'chick')
for food in restaurant:
    print(food)

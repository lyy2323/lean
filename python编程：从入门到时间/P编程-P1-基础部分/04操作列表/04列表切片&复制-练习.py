# 4.10 切片：
list = ['aaa', 'bbb', 'ccc', 'ddd', 'eee', 'fff', 'ggg', 'hhh']
lista = f'The first three items in the list are:{list[:3]}'
print(lista)
listb = f'Three items form the middle of the list are:{list[3:6]}'
print(listb)
listc = f'The last three items in the list are:{list[-3:]}'
print(listc)

# 4.11 你的披萨 我的披萨：
friend_list = list[:]
list.append('111')
friend_list.append('222')
print(f'My list is :')
# 打印披萨列表：
for list_pz in list[:]:
    print(f' - {list_pz}')
print(f'\nMy friend is :')
for list_fpz in friend_list[:]:
    print(f' - {list_fpz}')

# 使用多个循环，将课程中的代码修改为循环列表打印：
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
for mf in my_foods[:]:
    print(f' - {mf}')

print("\nMy friend's favorite foods are:")
for  ff in friend_foods[:]:
    print(f' - {ff}')

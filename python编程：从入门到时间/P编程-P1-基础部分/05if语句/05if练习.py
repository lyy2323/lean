# 以特殊方式跟管理员打招呼：
users = ['aaa', 'admin', 'bbb', 'ccc']
for user in users:
    if user == 'admin':
        print(f'Hello {user},would you like to see a status report?')
    else:
        print(f'Hello,{user},w')

# 列表为空是返回空白
users = []
if users:
    for user in users:
        print(f'{user},啊')
else:
    print('空白')

# 检查用户名：
current_users = ['aaa', 'bbb', 'ccc', 'ddd', 'eee', 'fff', 'ggg']
new_users = ['jjj', 'Ggg' ,'zzz', 'ttt', 'ddd']
current_users_lower = [user.lower() for user in current_users]
for users in new_users:
    if users.lower() in current_users_lower:
        print(f'{users}你不可以注册！')
    else:
        print(f'OK{users}')

# 序数：
number = list(range(1,10))
for numbers in number:
    if numbers == 1:
        numbers = '1st'
    elif numbers == 2:
        numbers = '2nd'
    elif numbers == 3:
        numbers = '3rd'
    else:
        numbers = f'{numbers}th'
    print(numbers)
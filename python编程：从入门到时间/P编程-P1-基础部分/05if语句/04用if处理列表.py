# 如果列表为空，则返回else，如果非空则执行if后结束：
requested_toppings =['111']
if requested_toppings:
    for requested_topping in requested_toppings:
        print(f'Adding {requested_topping}')
    print('\nFinished making your pizza!')
else:
    print('Are you sure you want a plain pizza?')

# 通过sort()方法，将列表永久的按字母正序排序或（reverse)倒序：
cars = ['bmw', 'audy', 'toyota', 'bens']
print(cars)
cars.sort()  # 永久按字母正向排序
print(cars)
cars.sort(reverse=True)  # 永久按字母反向排序
print(cars)
# 通过sorted()函数，进行临时排序：
cars = ['bmw', 'audy', 'toyota', 'bens']
print(sorted(cars))  # 按字母正向临时打印
print(sorted(cars, reverse=True))  # 按字母反向临时打印
print(cars)
#
cars.reverse()
print(cars)

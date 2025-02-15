# 4.3:数到20
for coumber in range(1,21):
    print(coumber)

# 4.5 1000求和
number = list(range(1,1001))
print(max(number))
print(min(number))
print(sum(number))

# 4.6 通过range的第三个参数——步长，实现奇数的打印
number = list(range(1,21,2))
for numbers in number:
    print(numbers)

# 4.7 3的倍数
number = list(range(3,31,3))
for numbers in number:
    print(numbers)

# 4.8 立方1
cubes = []
for number in range(1,11):
    cube = number **3
    cubes.append(cube)
for cube in cubes:
    print(cube)

# 立方2——使用推送式
cubes = [cube**3 for cube in range(1,11)]
print(cubes)
for cube in cubes:
    print(cube)

# 4.9 立方推送式
cubes = [c**3 for c in range(1,11)]
print(cubes)
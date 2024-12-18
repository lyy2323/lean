import random
print(random.seed(10))  # 以10为种子生成随机，但这个生成的随机是其实每一次都是固定的
print(random.random())
print(random.random())

print(random.randint(10,100))  # 随机生成10~100之间的整数

print(random.randrange(10,100,5))  # 随机在10~100之间，生成一个以5为步长的整数

print(random.getrandbits(4))  # 随机生成一个4比特长的整数

print(random.uniform(10,100))  # 随机生成一个10~100之间的小数

print(random.choice([1,2,3,4,5]))  # 随机在列表中选择一个数字生成

s = [1,2,3,4,5]
random.shuffle(s)
print(s)
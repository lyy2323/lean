# 序列类型是一个基类类型，包含：字符串类型、元组类型、列表类型

A = ['p','y',123]

print([234] in A)
print([234] not in A)
print(A + [234])
print(A.index('y'))  # 返回A序列中“y”这个元素第一次出现的序列位置
print(A.index('y',1,2))
print(A.count(123))  # 返回序列A中，123这个元素出现的总次数

print(A[-2])  # s[i]显示该序列的元素
print(A[::-1])  # 通过::-1，可以将序列中的元素反过来

a = 'python.123'
print(a[-2])  # s[i]显示该序列的元素
print(a[::-1])  # 使用::-1，对字符串也有效
print(len(a))  # 显示a 的序列长度

b = '123333456'
print(min(b))  # 显示该序列的最小元素，元素要科比
print(max(b))  # 显示该序列的最大元素，元素要可比

c = [1, 3, 4, 4, 4, 5, 6, 7]
d = c.count(4)
print(d)
e = c.index(4)  # 索引元素4在上面列表中出现的位置
print(e)
f = c.index(4, 0,6)  # index索引元素4在上面列表0~6位置中第一次出现的位置
print(f)


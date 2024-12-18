# 元组继承了序列类型的全部通用操作
# 元组因为创建后不能修改，因此没有特殊操作
# 使用或不使用小括号

# 元组是一种序列类型，一旦创建就不能被修改
# 使用小括号()或tuple()创建，元素间用逗号，分割

creature = 'cat', 'dog', 'tiger', 'human'
print(creature)
color = (0x001100, 'blue', creature)
print(color)
print(color[-1][1][2])  # 前一个-1是大序列中的最右侧元素，因为creature本身是个元组，所以后面的3是这个元素中的第三个
print(color[1][3])  # 前一个1是大序列中的最右侧元素，因为blue本身是个元组，所以后面的3是这个元素中的第三个
print(color[::-1])  # 元组类型可以使用::-1的序列切片倒叙排列


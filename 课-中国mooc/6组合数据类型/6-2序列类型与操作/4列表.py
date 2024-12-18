# 列表是一种序列类型，创建后可以被随意修改
# 使用方括号[]或者list()创建，元素间用逗号,分割
# 列表中各元素类型可以不同，无长度限制

ls = ['cat', 'dog', 'tiger', 1024]
ls[1:2] = [1,2,3,4]
print(ls)
del ls[::3]  # 删除ls列表中以3为步长的元素
print(ls)
print(ls*2)  # 将列表中的元素重复2次

ls.append(1234)  # 列表中增加1234
print(ls)
ls.insert(3,'human')  # 列表位置3的地方增加human
print(ls)
ls.reverse()  # 反转列表顺序
print(ls)

lt = []  # 创建一个空列表
print(lt)
lt += [1,2,3,4,50]  # 向lt列表中新增5个元素
print(lt)
lt[2] = 6  # 将位置2中的元素替换为元素6
print(lt)
lt.insert(2,9)  # 在列表位置2处，添加元素9
print(lt)
del lt[0]  # 删除第一个（位置0）的元素
print(lt)
del lt[0:3]  # 删除前前三个（位置0~3）的元素
print(lt)
print(0 in lt)  # 判断lt列表中有没有元素0
lt.append(0)  # 将元素0添加在lt列表中
print(lt)
print(lt.index(0))  # 索引0的位置
print(len(lt))  # 列表中元素的个数
print(max(lt))  # 列表中最大的元素
lt.clear()  # 清空列表中的元素
print(lt)
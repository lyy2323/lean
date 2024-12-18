# 集合是使用{}或set()函数来创建的
# 集合之间的操作包含：交-&、并-|、差--、补-^、比较>=<
# 特点
# 集合用大括号表示，元素间用逗号间隔
# 集合中每个元素唯一，不存在相同元素
# 集合元素之间无序
#
# 集合的两个重要作用：
# 1、包含关系比较；2、去重

a = {'python',123,(456,'run')}
print(a)

a.copy()
print(a)

print(len(a))

b = set('123pthon')
print(b)

b.add('456')
print(b)

b.discard('2')
print(b)

b.remove('3')
print(b)

c = b.pop()  # 移除并返回b中的随即一个元素
print(b)  # 移除b中一个随机元素
print(c)  # 返回b中的一个随机元素

b.clear()  # 清空b
print(b)  # 返回结果为set()

A = {'p','y',123}
for item in A:
    print(item, end='')
print(A)
try:
    while True:
        print(A.pop(), end='')
except:
    pass
print()
print(A)

# 利用集合“无重复元素”的特点，帮助列表去重：
ls = ['p','p','y','y',123]
s = set(ls)  # 先将上面的列表转为集合
ls = list(s)  # 再将上面的集合转回为列表，就完成了
print(ls)
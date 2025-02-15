name = ['张三', '李四', '王二', 'mary']
print(name[-1].title())
print(name[0])
message = f'{name[1]},在的'
print(message)
print(f'{name[3].upper()},是的')
name[0] = '钱五'
print(name)
name.append('666')
print(name)

names = []
names.append('111')
names.append('222')
names.append('333')
names.append('444')
print(names)
del names[1:3]
print(names)
a = names.pop(1)
print(names)
print(a)

names.append('555')
names.append('666')
names.append('777')
print(names)
new_names = names[1]
names.remove(new_names)
print(names)
print(new_names)
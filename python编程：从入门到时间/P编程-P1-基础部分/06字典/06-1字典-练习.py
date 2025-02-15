# 人——使用字典存储信息，包括名、姓、年龄、居住地。。
person = {'frist_name':'dehua', 'last_name':'Liu', 'age':50, 'city':'hongkong'}
print(person["frist_name"])
print(person["last_name"])
print(person.get('age'))
print(person.get('school','no one'))

# 喜欢的数：
favorite_number = {
    'aaa':111,
    'bbb':222,
    'ccc':333,
    }
aaas = favorite_number['aaa']
print(f'My favorite is{aaas}')
print(favorite_number.get('ddd'))

# 词汇表：
language = {'dog': '狗',
            'food': '食物',
            'foot': '脚',
            'bottle':'bottle-瓶子'
            }
word = 'dog'
print(f'{word.title()} :{language[word]}')
word = 'food'
print(f'{word.title()}: {language[word]}')
word = 'foot'
print(f'{word.title()}: {language[word]}')
word = 'bottle'
print(f'{word.title()}: {language[word].title()}')

# 遍历键值对，并使用items()方法，分别打印键和值
for k, v in language.items():
    print(f'k:{k}')
    print(f'v:{v}')
    print(k,v)

for name in language:
    print(name.title())

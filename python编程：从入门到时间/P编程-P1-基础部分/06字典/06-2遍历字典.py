language = {'dog': '狗',
            'food': '食物',
            'foot': '脚',
            'bottle':'bottle-瓶子'
            }
friends = ['dog', 'foot', 'bottle']
for name in language.keys():
    print(f'Hi {name.title()}')

    if name in friends:
        languages = language[name].title()
        print(f'\t{name.title()}, I see you love {languages}')

for name in language.keys():
    print(name.title())

for word,lan in language.items():
    print(f'\n{word},目标{lan}')

# 6.5 河流

river = {'huanghe': 'china',
         'duonaohe': 'germary',
         'laiyinghe':'french'
         }
for name in river.keys():
    print(f'\nRiver {name.title()}')
for name in river.values():
    print(f'\nN {name.title()}')
for nemas in river.items():
    print(f'\nitems: {nemas}')

# 6.4 调查（沿用上面的字典）：
favorite = ['huanghe', 'changjiang', 'duonaohe']
for fa in favorite:
    if fa in river.keys():
        print(f'Welcome！{fa.title()}')
    else:
        print(f'Next,{fa.title()}')
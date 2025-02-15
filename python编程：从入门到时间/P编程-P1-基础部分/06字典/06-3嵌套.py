language = {'dog': ['狗', '犬', '小狗'],
            'food': ['食物', '食品', '吃的'],
            'foot': ['脚'],
            'bottle':['bottle-瓶子'],
            }
for lan_name, l_name in language.items():
    print(f'{lan_name.title()}xx的分类是：',end="")
    if len(l_name) == 1:
        for l in l_name:
            print(f'{l}')
    else:
        for l in l_name:
            print(f'\n\t{l}')
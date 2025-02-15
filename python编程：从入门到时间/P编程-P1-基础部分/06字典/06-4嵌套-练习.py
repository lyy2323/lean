# 6.7 人们
people = {
        'make': {
            'name_f':'dehua',
            'name_l': 'liu',
            'city': 'hongkong'
        },
        'jeke':{
            'name_f': 'xueyou',
            'name_l':'zhang',
            'city':'hongkong',
        },
    }
for name, info in people.items():
    full_name = f'{info["name_f"]} {info["name_l"]}'
    location = f'{info["city"]}'
    print(f'User:{name.title()}')
    print(f'\t{full_name.title()}')
    print(f'\t{location.title()}')

print('\n=======++分隔符++=======\n')

# 6.8 宠物
pets = {'dog': {
            'sort': '毛绒',
            'people': 'jeke',
            },
        'fish': {
            'sort': 'water',
            'people': 'make',
        },
    }
for name, info in pets.items():
    print(f'Pet:{name.title()}:')
    for i in info.values():
       print(f'\t{i}')

print('\n=======++分割线++=======\n')

# 6.9 喜欢的地方：
favorite_places = {
        'jeke': ['香港', '澳门', '台湾'],
    'make': ['上海'],
    'tangmo': ['纽约', '阿姆斯特丹'],
        }
for name, info in favorite_places.items():
    print(f'{name.title()}喜欢：')
    for i in info:
        print(f'\t{i}')

print('\n=======++分割线++=======\n')

# 6.10 喜欢的数字
favorite_number = {
    'aaa':[111,9,900],
    'bbb':[222,333,11],
    'ccc':[333]
    }
for name, num in favorite_number.items():
    print(f'{name.title()}')
    for n in num:
        print(f'\t{n}')

print('\n=======++分割线++=======\n')

# 6.11 城市：
cities = {
    "伦敦": {'country':'英国',
             'population': '1000万',
             'fact': '所在区域欧洲'
             },
"纽约": {'country': '美国',
         'population': '2000万',
         'fact': '所在区域北美洲'
         },
"北京": {'country': '中国',
         'population': '1800万',
         'fact': '所在区域亚洲'
         },
}
for city, info in cities.items():
    country = info['country'].title()
    population = info['population'].title()
    fact = info['fact'].title()
    print(f'{city}:')
    print(f'\tcountry:{country}')
    print(f'\tpopulation:{population}')
    print(f'\tfact:{fact}')
# T恤
def make_shirt(size,word):
    print(f"T恤的大小是{size},需要打印的文字是{word}")
make_shirt("12",'"这是最好的"')
make_shirt("13", "\"这不是最好的\"")
make_shirt(word="这是关键字", size="11")
make_shirt("12","")

# 大号T恤
def make_shirt(size,word="I love Python!"):
    print(f"T恤的大小是{size},需要打印的文字是{word}")
make_shirt("12")
make_shirt("13")
make_shirt(word="这是关键字", size="11")
make_shirt("12","这是修改后的")

def describe_city(city, county="china"):
    print(f"{city} is in {county}")
describe_city("beijing")
describe_city("california", "USA")

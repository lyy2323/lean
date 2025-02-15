# 7.8 熟食店
sandwich_orders = ["aaa", "bbb", "ccc", "bbb", "ddd"]
finished_sandwiches = []
while sandwich_orders:
    sand = sandwich_orders.pop()
    print(f"这个好了{sand}")
    finished_sandwiches.append(sand)
print(f"{finished_sandwiches}\n")


#  7.9 延用上面的列表，并通过while循环剔除“bbb”
sandwich_orders = ["aaa", "bbb", "ccc", "bbb", "ddd"]
print("抱歉，bbb没有了")
while "bbb" in sandwich_orders:
    sandwich_orders.remove("bbb")
print(sandwich_orders)

# 7.10 梦想中的度假圣地
places = {}
places_active = True

while places_active:
    name = input("what your name?")
    place = input("Where are you？")

    places[name] = place

    next = input("继续吗？(yes/no)")
    if next == "no":
        places_active = False

print("---存储如下---")
for name, place in places.items():
    print(f"{name}想去的地方是{place}")

from ast import increment_lineno


class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    def describe_restaurant(self):
        print(f"{self.restaurant_name} 属于 {self.cuisine_type}!")
    def open_restaurant(self):
        print(f"{self.restaurant_name} is open!")
    def set_number_served(self, number_served):
        self.number_served = number_served
    def increment_number_served(self, person):
        self.number_served += person
my_restaurant = Restaurant("鱼头当家", "中餐")
print(f"{my_restaurant.restaurant_name} is {my_restaurant.cuisine_type}")
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()
my_restaurant.increment_number_served(12)
my_restaurant.number_served = 12
print(f"\n就餐人数是{my_restaurant.number_served}人")
my_restaurant.increment_number_served = 5
print(f"\n新的人数是{my_restaurant.increment_number_served}人")

print("11111")

home_restaurant = Restaurant("家门口的烧烤", "烧烤")
print(f"{home_restaurant.restaurant_name} 是家门口的一家{home_restaurant.cuisine_type}！")
home_restaurant.describe_restaurant()
home_restaurant.open_restaurant()

shopping_restaurant = Restaurant("海底捞", "火锅店")
print(f"{shopping_restaurant.restaurant_name} is shopping mall 中的{shopping_restaurant.cuisine_type}")
shopping_restaurant.describe_restaurant()
shopping_restaurant.open_restaurant()


"""答案"""

class Restaurant:
    def __init__(self, name, cuisine_type):
        """初始化餐馆"""
        self.name = name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    def describe_restaurant(self):
        """显示餐馆信息摘要"""
        msg = f"{self.name} serves wonderful {self.cuisine_type}."
        print(f"\n{msg}")
    def set_number_served(self, number_served):
        """让用户能够设置就餐人数"""
        self.number_served = number_served
    def increment_number_served(self, additional_served):
        """让用户能够增加就餐人数"""
        self.number_served += additional_served
restaurant = Restaurant("新海底捞", "火锅店")
restaurant.describe_restaurant()
print(f"刚开始的就餐人数是：{restaurant.number_served}")
restaurant.set_number_served(50)
print(f"\n新增了{restaurant.number_served}")
restaurant.increment_number_served(100)
print(f"\n又增加到了：{restaurant.number_served}")
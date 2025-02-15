class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    def describe_restaurant(self):
        print(f"{self.restaurant_name} 属于 {self.cuisine_type}!")
    def open_restaurant(self):
        print(f"{self.restaurant_name} is open!")
my_restaurant = Restaurant("鱼头当家", "中餐")
print(f"{my_restaurant.restaurant_name} is {my_restaurant.cuisine_type}")
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()

home_restaurant = Restaurant("家门口的烧烤", "烧烤")
print(f"{home_restaurant.restaurant_name} 是家门口的一家{home_restaurant.cuisine_type}！")
home_restaurant.describe_restaurant()
home_restaurant.open_restaurant()

shopping_restaurant = Restaurant("海底捞", "火锅店")
print(f"{shopping_restaurant.restaurant_name} is shopping mall 中的{shopping_restaurant.cuisine_type}")
shopping_restaurant.describe_restaurant()
shopping_restaurant.open_restaurant()
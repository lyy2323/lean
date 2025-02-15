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

class IceCreamStand(Restaurant):
	def __init__(self, name, cuisine_type, flavors):
		super().__init__(name, cuisine_type)
		self.flavors = flavors
	def d_flavors(self):
		print(f"\n我们提供如下{self.cuisine_type}：")
		for f in self.flavors:
			print(f"\t-{f}")
i_rest = IceCreamStand("蜜雪冰城", "冰激凌", ["sdfsdf", "adfad", "gd"])
i_rest.d_flavors()


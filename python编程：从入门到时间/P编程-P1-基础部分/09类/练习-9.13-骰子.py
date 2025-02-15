# 练习9.13 骰子
from random import randint

class Die:
    def __init__(self, sides=6):
        self.sides = sides
    def roll_die(self):
        return randint(1, self.sides)

six = Die()

results = []
for roll_num in range(10):
    result = six.roll_die()
    results.append(result)
print(results)

ten = Die(sides=10)
results = []
for roll_num in range(10):
    result = ten.roll_die()
    results.append(result)
print(results)

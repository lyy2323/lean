from car import Car

class Battery(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.age = 0
    def c_battery(self):
        print(f"\n里程是{self.make},{self.age}")

my_b = Battery("jk", "123", "22")
my_b.c_battery()
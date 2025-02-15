class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def sit(self):
        print(f"{self.name} is siting!")
    def roll_over(self):
        print(f"{self.name} is roll_over!")
my_dog = Dog("canty", 6)
print(f"{my_dog.name} is {my_dog.age}")
my_dog.sit()
my_dog.roll_over()
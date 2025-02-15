from numpy.ma.core import logical_not


class User:
    def __init__(self, first_name, last_name, username, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.age = age
        self.login_attempts = 0
    def describe_user(self):
        print(f"{self.first_name.title()} {self.last_name.title()} 是正直的！")
        print(f"{self.username} 的邮箱是{self.email}")
    def greet_user(self):
        print(f"{self.username} 是 {self.age}")
    def increment_login_attempts(self):
        self.login_attempts += 1
    def rest_login_attempts(self):
        self.login_attempts = 0



me = User("jack", "canty", "JC", "1223@123.com", 26)
me.describe_user()
me.greet_user()
print(f"\n初始的是{me.login_attempts}")
me.increment_login_attempts()
print(f"\n增加了：{me.login_attempts}")
me.increment_login_attempts()
print(f"\n第二次调用：{me.login_attempts}")
me.rest_login_attempts()
print(f"\n又回到初始状态：{me.login_attempts}")

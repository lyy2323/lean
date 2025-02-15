class User:
    def __init__(self, first_name, last_name, username, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.age = age
    def describe_user(self):
        print(f"{self.first_name.title()} {self.last_name.title()} 是正直的！")
        print(f"{self.username} 的邮箱是{self.email}")
    def greet_user(self):
        print(f"{self.username} 是 {self.age}")
me = User("jack", "canty", "JC", "1223@123.com", 26)
me.describe_user()
me.greet_user()
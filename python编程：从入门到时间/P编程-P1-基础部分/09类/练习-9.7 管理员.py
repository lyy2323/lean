class User:
    def __init__(self, first_name, last_name, username, email, age, location):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.age = age
        self.location = location.title()
        self.login_attempts = 0
    def describe_user(self):
        """显示用户信息摘要"""
        print(f"\n{self.first_name.title()} {self.last_name.title()} 是正直的！")
        print(f"{self.username} 的邮箱是{self.email}")
        print(f"location：{self.location}")
    def greet_user(self):
        """向用户发送个性化问候"""
        print(f"\nWelcome back {self.username}")
    def increment_login_attempts(self):
        """将属性login_attempts的值加1"""
        self.login_attempts += 1
    def rest_login_attempts(self):
        """将login_attempts重置为0"""
        self.login_attempts = 0

class Admin(User):
    def __init__(self, first_name, last_name, username, email, age, location):
        super().__init__( first_name, last_name, username, email, age, location)
        self.privileges = []

    def show_privileges(self):
        print(f"\n管理员权限是：")
        for p in self.privileges:
            print(f"-{p}")
eric = Admin("eric", "mate", "lianmong", "123@222.com", 25, "alaska")
eric.privileges = ["dsfs", "fds", "123"]
eric.show_privileges()
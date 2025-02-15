from pathlib import Path
import json

def get_stored_user_info(path):
    """获取存储的用户信息（如果有的话）"""
    if path.exists():
        contents = path.read_text(encoding='utf-8')
        user_dict = json.loads(contents)
        return user_dict
    else:
        return None

def get_new_user_info(path):
    """从用户那里获取信息"""
    username = input("你的名字是？")
    game = input("你最喜欢的是？")
    animal = input("你最喜欢的动物是？")

    user_dict = {
        "username": username,
        "game": game,
        "animal": animal
    }
    contents = json.dumps(user_dict)
    path.write_text(contents, encoding='utf-8')
    return user_dict

def greet_user():
    """根据用户的新老情况发出不同的问候，并在用户为老用户时显示其信息"""
    path = Path("username.json")
    user_dict = get_stored_user_info(path)
    if user_dict:
        correct = input(f"你的名字是{user_dict['username']}？")
        if correct == "y":
            print(f"欢迎回来，{user_dict['username']}!")
        else:
            username = get_new_user_info(path)
            print(f"我们会记住你的，{user_dict['username']}!")
            print(f"希望你经常玩{user_dict['game']}")
            print(f"和你的{user_dict['animal']}")
    else:
        user_dict = get_new_user_info(path)
        msg = f"我们会记得你的，{user_dict['username']},我们知道你喜欢{user_dict['game']}和{user_dict['animal']}"
        print(msg)

greet_user()
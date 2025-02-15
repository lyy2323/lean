prompt = "\nTell me something ,and..."
prompt += "\nEnter 'quit' to end the program"

action = True
while action:
    message = input(prompt)
    if message == "quite":
        action = False
        print('结束')
    elif message == '000':
        print('jieshu')
        break
    else:
        print(message)

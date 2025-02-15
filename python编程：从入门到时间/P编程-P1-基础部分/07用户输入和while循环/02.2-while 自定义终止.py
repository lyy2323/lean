prompt = "\nTell me something ,and..."
prompt += "\nEnter 'quit' to end the program"

message = ""
while message != "quit":
    message = input(prompt)
    print(message)

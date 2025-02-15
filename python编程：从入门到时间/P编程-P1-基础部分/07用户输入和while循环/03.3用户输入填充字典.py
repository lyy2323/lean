"""
responses = {}
polling_active = True

while polling_active:
    name = input("\nWhat is your name?")
    response = input("Which mounatin would you like to climb someday?")

    responses[name] = response

    repeat = input("Would you like to let another person respond (yes/no)")
    if repeat == "no":
        polling_active = False

print("\n--- poll Results ---")
for name,response in responses.items():
    print(f"{name},would like to climb {response}")
"""

responses = {}

while True:
    name = input("\nWhat is your name?")
    response = input("Which mounatin would you like to climb someday?")

    responses[name] = response

    repeat = input("Would you like to let another person respond (yes/no)")
    if repeat == "no":
        break

print("\n--- poll Results ---")
for name,response in responses.items():
    print(f"{name},would like to climb {response}")

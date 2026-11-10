import random

people = []

print("===== Family Lottery =====")
number = int(input("How many people? "))

for i in range(number):
    name = input("Enter person's name: ")
    people.append(name)

while True:
    print("\n1- Show People")
    print("2- Start Lottery")
    print("0- Exit")

    choice = input("Choose: ")

    match choice:
        case "1":
            print("Family Members:")
            for person in people:
                print(person)

        case "2":
            if len(people) == 0:
                print("List is empty!")
            else:
                winner = random.choice(people)
                print("The Winner Is:", winner)

        case "0":
            print("Goodbye!")
            break

        case _:
            print("Invalid Choice!")

import random

people = []
prizes = []

print("===== People List =====")
number = int(input("How many people? "))

for i in range(number):
    name = input("Enter person's name: ")
    people.append(name)

print("\n===== Prize List =====")
for i in range(number):
    prize = input("Enter prize: ")
    prizes.append(prize)

while True:
    print("\n1- Show People")
    print("2- Show Prizes")
    print("3- Start Lottery")
    print("0- Exit")

    choice = input("Choose: ")

    match choice:
        case "1":
            print(people)

        case "2":
            print(prizes)

        case "3":
            shuffled_people = people.copy()
            shuffled_prizes = prizes.copy()

            random.shuffle(shuffled_people)
            random.shuffle(shuffled_prizes)

            print("\n===== Lottery Results =====")
            for i in range(number):
                print(shuffled_people[i], "won:", shuffled_prizes[i])

        case "0":
            print("Goodbye!")
            break

        case _:
            print("Invalid Choice!")

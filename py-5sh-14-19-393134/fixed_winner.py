people = []

number = int(input("How many people? "))

for i in range(number):
    name = input("Enter name: ")
    people.append(name)

print("\nFamily Members:")
print(people)

fixed_winner = input("\nEnter the name of fixed winner: ")

match fixed_winner in people:
    case True:
        print("\nThe Winner Is:", fixed_winner)
    case False:
        print("This person is not in the list!")

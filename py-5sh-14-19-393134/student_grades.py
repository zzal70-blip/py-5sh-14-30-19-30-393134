print("===== Student Grades =====")

name = input("Enter name: ")
family = input("Enter family: ")

python = float(input("Enter Python grade: "))
java = float(input("Enter Java grade: "))
html = float(input("Enter HTML grade: "))

average = (python + java + html) / 3

print("\n===== Student Report =====")
print("Name:", name)
print("Family:", family)
print("Python:", python)
print("Java:", java)
print("HTML:", html)
print("Average:", average)

match average:
    case x if x >= 18:
        print("Excellent!")
    case x if x >= 15:
        print("Very Good!")
    case x if x >= 12:
        print("Good!")
    case x if x >= 10:
        print("Passed!")
    case _:
        print("Failed!")

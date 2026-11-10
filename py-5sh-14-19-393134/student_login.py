students = [
    {
        "name": "Ali Ahmadi",
        "username": "ali123",
        "password": "1234",
        "python": 18,
        "java": 17,
        "html": 20,
        "js": 19
    }
]

while True:
    print("\n===== Student System =====")
    print("1- Login")
    print("2- Register")
    print("3- Show Students")
    print("0- Exit")

    choice = input("Choose: ")

    match choice:
        case "1":
            username = input("Username: ")
            password = input("Password: ")
            found = False

            for student in students:
                if student["username"] == username and student["password"] == password:
                    print("Login Successful!")
                    print("Name:", student["name"])
                    found = True
                    break

            if not found:
                print("Username or Password is incorrect!")

        case "2":
            name = input("Enter name and family: ")
            username = input("Enter username: ")
            password = input("Enter password: ")

            python = float(input("Python grade: "))
            java = float(input("Java grade: "))
            html = float(input("HTML grade: "))
            js = float(input("JavaScript grade: "))

            exists = False
            for student in students:
                if student["username"] == username:
                    exists = True
                    break

            if exists:
                print("This username already exists!")
            else:
                students.append({
                    "name": name,
                    "username": username,
                    "password": password,
                    "python": python,
                    "java": java,
                    "html": html,
                    "js": js
                })
                print("Registration Successful!")

        case "3":
            for student in students:
                print(student)

        case "0":
            print("Goodbye!")
            break

        case _:
            print("Invalid Choice!")

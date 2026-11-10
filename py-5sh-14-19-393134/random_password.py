import string
import secrets

while True:
    print("\n===== Password Generator =====")
    print("1- Generate Password")
    print("0- Exit")

    choice = input("Choose: ")

    match choice:
        case "1":
            upper = secrets.choice(string.ascii_uppercase)
            lower = secrets.choice(string.ascii_lowercase)
            digit = secrets.choice(string.digits)
            special = secrets.choice("!@#$%^&*()_+-=")

            all_chars = (
                string.ascii_letters
                + string.digits
                + "!@#$%^&*()_+-="
            )

            password = [upper, lower, digit, special]

            for i in range(14):
                password.append(secrets.choice(all_chars))

            secrets.SystemRandom().shuffle(password)
            password = "".join(password)

            print("Random Password:", password)
            print("Length:", len(password))

        case "0":
            print("Goodbye!")
            break

        case _:
            print("Invalid Choice!")

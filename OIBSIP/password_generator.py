import random
import string

print("===== RANDOM PASSWORD GENERATOR =====")

while True:
    try:
        length = int(input("\nEnter password length (minimum 8): "))

        if length < 8:
            print("Password length must be at least 8.")
            continue

        uppercase = input("Include uppercase letters? (yes/no): ").lower()
        lowercase = input("Include lowercase letters? (yes/no): ").lower()
        numbers = input("Include numbers? (yes/no): ").lower()
        symbols = input("Include symbols? (yes/no): ").lower()

        characters = ""
        selected_types = []

        if uppercase == "yes":
            characters += string.ascii_uppercase
            selected_types.append(string.ascii_uppercase)

        if lowercase == "yes":
            characters += string.ascii_lowercase
            selected_types.append(string.ascii_lowercase)

        if numbers == "yes":
            characters += string.digits
            selected_types.append(string.digits)

        if symbols == "yes":
            characters += string.punctuation
            selected_types.append(string.punctuation)

        if len(selected_types) < 2:
            print("Please select at least 2 character types.")
            continue

        password = []

        # Add at least one character from each selected type
        for group in selected_types:
            password.append(random.choice(group))

        # Fill the remaining password length
        for i in range(length - len(password)):
            password.append(random.choice(characters))

        random.shuffle(password)

        final_password = "".join(password)

        print("\nYour Generated Password:", final_password)

        choice = input("\nGenerate another password? (yes/no): ").lower()

        if choice != "yes":
            print("Thank you for using Password Generator!")
            break

    except ValueError:
        print("Invalid input! Please enter a valid number.")
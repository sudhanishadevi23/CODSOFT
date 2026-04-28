# Password Generator Application
# Author: Your Name
# Description: Generates strong random passwords based on user preferences

import random
import string


def generate_password(length, use_upper, use_digits, use_symbols):
    characters = string.ascii_lowercase  # always include lowercase

    if use_upper:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    # Generate password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password


def main():
    print("====== PASSWORD GENERATOR ======")

    try:
        length = int(input("Enter password length: "))
        if length <= 0:
            print("Length must be greater than 0.")
            return
    except ValueError:
        print("Please enter a valid number.")
        return

    # Complexity options
    use_upper = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_digits = input("Include numbers? (y/n): ").lower() == 'y'
    use_symbols = input("Include special characters? (y/n): ").lower() == 'y'

    password = generate_password(length, use_upper, use_digits, use_symbols)

    print("\nGenerated Password:")
    print(password)


if __name__ == "__main__":
    main()

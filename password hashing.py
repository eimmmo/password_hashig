import random
import string
import os

characters = list(string.ascii_letters + string.digits + string.punctuation + ' ')
keys = characters.copy()
random.shuffle(keys)

def hashing_password(password):
    hashed_password = ""
    for char in password:
        if char in characters:
            hashed_password += keys[characters.index(char)]
        else:
            hashed_password += '?'
    return hashed_password

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def password_verification_with_attempts():
    max_attempts = 3
    attempts = 0

    while True:
        input_password = input("Enter the password to set: ").strip()
        if input_password:
            break
        print("Password cannot be empty. Try again.\n")

    hashed_first_password = hashing_password(input_password)
    print("Password saved successfully.\n")
    input("Press Enter to continue...")
    clear_screen()

    print("Please re-enter the password to verify.")
    print(f"You have {max_attempts} attempts.\n")

    while attempts < max_attempts:
        tested_password = input(f"Attempt {attempts + 1}/{max_attempts}: ").strip()

        if not tested_password:
            print("Password cannot be empty. Try again.")
            attempts += 1
            continue

        hashed_tested_password = hashing_password(tested_password)

        if hashed_tested_password == hashed_first_password:
            print("\nPassword is correct. Access granted!")
            return
        else:
            attempts += 1
            remaining = max_attempts - attempts
            if remaining > 0:
                print(f"Wrong password. {remaining} attempts left.\n")
            else:
                print("\nToo many failed attempts. Access denied.")

password_verification_with_attempts()
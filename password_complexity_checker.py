# Author: Reginald Andre Evangelista
# Position: Intern for Cyber Security
# Company: Prodigy InfoTech

import re
SPECIAL = "!@#$%^&*()-_=+,<.>/?;:'\"[{]}\\|"

def check_password(password):
    strength = ''
    requirements = []

    # Different password crtierias for checker
    check_length = len(password) >= 8
    check_upper = any(char.isupper() for char in password)
    check_lower = any(char.islower() for char in password)
    check_digit = any(char.isdigit() for char in password)
    check_special = False
    for char in password:
        if char in SPECIAL:
            check_special = True
            break

    if not check_length:
        requirements.append("Length must be 8 or more characters.")
    if not check_upper:
        requirements.append("Must include uppercase letters (A-Z).")
    if not check_lower:
        requirements.append("Must include lowercase letters (a-z).")
    if not check_digit:
        requirements.append("Must include a number (0-9).")
    if not check_special:
        requirements.append("Must include a special character.")
    
    if check_length and check_upper and check_lower and check_digit and check_special:
        strength = 'Strong'
    elif check_length and (check_upper or check_lower or check_digit or check_special):
        strength = 'Medium'
    elif check_length:
        strength = 'Weak'
    else:
        strength = 'Very Weak'

    print("Your password is: ", strength)
    if(len(requirements) == 0):
        print("Great job! You have a very complex password.")
    else:
        print("Here are some suggestions to make your password stronger: ")
        for reqs in requirements:
            print("\t- " + reqs)

def main():
    password = input("Input the password you want to be checked: ")
    check_password(password)

if __name__ == "__main__":
    main()

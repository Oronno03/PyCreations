import random
import string


def gen_pass(length, nums=False, special_chars=False):
    letters = string.ascii_letters
    digits = string.digits
    special_chars_ = string.punctuation

    chars = letters
    if nums:
        chars += digits
    if special_chars:
        chars += special_chars_

    pwd = ""
    meets_criteria = False

    while not meets_criteria:
        pwd = random.sample(chars, length)

        meets_criteria = True
        has_num = any(char.isdigit() for char in pwd)
        has_special = any(char in special_chars_ for char in pwd)

        if nums:
            meets_criteria = has_num and meets_criteria
        if special_chars:
            meets_criteria = has_special and meets_criteria

    return "".join(pwd)


def ask():
    print("="*40)
    print("Password Generator".center(40))
    print("Type Q to quit anytime".center(40))
    print("="*40)
    
    while True:
        print("What length do you want?")
        length = input("> ")

        if length.lower() == 'q':
            break
        elif not length.isdigit():
            print("Please provide a valid length")
            continue
        else:
            length = int(length)

        has_num = input("Do you want to have numbers? ([y]/n) ").lower() != "n"
        has_chars = (
            input("Do you want to have special characters? ([y]/n) ").lower() != "n"
        )
        pwd = gen_pass(length, has_num, has_chars)
        print(f"Your generated password is: {pwd}\n")


ask()
input("Thanks for using!")

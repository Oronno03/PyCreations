import random

high, low = 100, 1
num = random.randint(low, high)
tries = 0
max_tries = 10

print(f"I am thinking of a number between {low} to {high}")
while tries < max_tries:
    print(f"You have {max_tries - tries} tries left to guess.")
    print("Enter your guess")
    try:
        guess = int(input("> "))
        if not low <= guess <= high:
            raise ValueError
    except:
        print(f"Please enter a valid guess. ({low}-{high})")
        continue
    tries += 1
    if guess == num:
        print(f"You got it in {tries} tries! Congrats!")
        quit()

    elif guess < num:
        print("I am thinking of a bigger number")
    
    elif guess > num:
        print("I am thinking of a smaller number")

print(f"I was thinking of {num}. You could not guess it in {max_tries} tries")
print("Better luck next time")
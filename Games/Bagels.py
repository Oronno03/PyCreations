import random

NUM_DIGITS = 3 
MAX_GUESSES = 10  



class Bagels:

    def __init__(self, num_digits = NUM_DIGITS, max_guesses = MAX_GUESSES):
        self.num_digits = num_digits
        self.max_guesses = max_guesses

    def generate_secret_number(self):
        nums = list("123456789")
        random.shuffle(nums)

        return "".join(nums.pop() for _ in range(self.num_digits))

    def play(self):
        while True:
            secret = self.generate_secret_number()
            print(
                f"I am thinking of a {self.num_digits} digit number\n"
                "Try to guess the number\n"
                "Here are some clues: \n"
                "When I say: \t That means:\n"
                "  Pico :  \t   One digit is correct but in the wrong position\n"
                "  Fermi:  \t   One digit is correct and in the right position\n"
                "  Bagel:  \t   No digit is correct"
            )
            print(
                "For example, if the secret number was 248 and your guess was 843,"
                "the clues would be Fermi Pico\n"
            )
            guesses = 1
            print("I have thought of the number")
            print(f"You have {self.max_guesses} to guess it!")

            while guesses <= self.max_guesses:
                guess = ""
                while len(guess) != self.num_digits or not guess.isdecimal():
                    print(f"Guess #{guesses}")
                    guess = input("> ")

                clues = self.get_clues(guess, secret)
                print(*clues)
                guesses += 1

                if guess == secret:
                    print("Congratulations! You've guessed the number correctly.")
                    break

                if guesses > self.max_guesses:
                    print("You have ran out of guesses")
                    print(f"The answer was {secret}")
                    break

            play_again = input("Do you want to play again? ([yes]/no): ")
            if play_again.lower() in "no":
                break

    def get_clues(self, guess, secret_num):

        if guess == secret_num:
            return ["You got it"]

        clues = []
        for i, num in enumerate(guess):
            if num == secret_num[i]:
                clues.append("Fermi")

            elif num in secret_num:
                clues.append("Pico")

        return clues or ["Bagel"]


if __name__ == "__main__":
    bagels = Bagels()
    bagels.play()
    input("Thanks for playing. Press Enter to QUIT.")

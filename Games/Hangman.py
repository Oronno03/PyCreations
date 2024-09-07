import random
import os

words = [
    "python",
    "java",
    "kotlin",
    "javascript",
    "hangman",
    "developer",
    "github",
    "flask",
    "django",
]

HANGMAN_STAGES = [
    """
    +---+
    |   |
        |
        |
        |
        |
   =========
    """,
    """
    +---+
    |   |
    O   |
        |
        |
        |
   =========
    """,
    """
    +---+
    |   |
    O   |
    |   |
        |
        |
   =========
    """,
    """
    +---+
    |   |
    O   |
   /|   |
        |
        |
   =========
    """,
    """
    +---+
    |   |
    O   |
   /|\\  |
        |
        |
   =========
    """,
    """
    +---+
    |   |
    O   |
   /|\\  |
   /    |
        |
   =========
    """,
    """
    +---+
    |   |
    O   |
   /|\\  |
   / \\  |
        |
   =========
    """,
]


def clear_terminal():
    os.system("cls" if os.name == "nt" else "clear")


def get_random_word():
    return random.choice(words)


def display_hangman(tries):
    print(HANGMAN_STAGES[tries])


def play_hangman():
    word = get_random_word()
    word_letters = set(word)
    guessed_letters = set()
    incorrect_guesses = set()
    tries = 6

    print("Welcome to Hangman!")

    while tries > 0:
        clear_terminal()
        print(f"\nYou have {tries} tries left.")
        display_hangman(6 - tries)

        word_display = [letter if letter in guessed_letters else "_" for letter in word]
        print("Word: " + " ".join(word_display))

        guess = input("\nGuess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a valid single letter.")
            input("Press Enter to continue...")
            continue

        if guess in guessed_letters or guess in incorrect_guesses:
            print(f"You already guessed the letter '{guess}'. Try again.")
            input("Press Enter to continue...")
            continue

        if guess in word_letters:
            guessed_letters.add(guess)
            word_letters.remove(guess)
            print(f"Good job! '{guess}' is in the word.")
        else:
            tries -= 1
            incorrect_guesses.add(guess)
            print(f"Oops! '{guess}' is not in the word.")

        input("Press Enter to continue...")

        if not word_letters:
            clear_terminal()
            print(f"\nCongratulations! You guessed the word '{word}'. You win!")
            break
    else:
        clear_terminal()
        display_hangman(6)
        print(f"\nGame Over! The word was '{word}'. Better luck next time!")


if __name__ == "__main__":
    play_hangman()

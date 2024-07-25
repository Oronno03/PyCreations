import random


class GuessTheNumber:
    def __init__(self):
        self.print_header("** Guess The Number **", 40)
        self.wins = 0
        self.matches = 0
        self.set_difficulty("EASY")
        self.set_lower_bound(1)
        self.set_higher_bound(100)
        self.set_max_tries(10)

    def print_header(self, text, size):
        print("=" * size)
        print(text.center(size))
        print("=" * size)

    def set_difficulty(self, difficulty=None):
        if difficulty:
            self.difficulty = difficulty
            return

        while True:
            print("Choose your difficulty level:")
            print("1. Kid, 1-100 in 100 tries")
            print("2. Easy, 1-100 in 10 tries")
            print("3. Medium, 1-1000 in 10 tries")
            print("4. Hard, 1-10000 in 10 tries")
            print("You can also manually change the numbers and tries")
            response = input("> ")

            match response:
                case "1":
                    self.difficulty = "KID"
                    self.set_lower_bound(1)
                    self.set_higher_bound(100)
                    self.set_max_tries(100)
                    print("Difficulty level has been set to 'KID'")
                    break
                case "2":
                    self.difficulty = "EASY"
                    self.set_lower_bound(1)
                    self.set_higher_bound(100)
                    self.set_max_tries(10)
                    print("Difficulty level has been set to 'EASY'")
                    break
                case "3":
                    self.difficulty = "MEDIUM"
                    self.set_lower_bound(1)
                    self.set_higher_bound(1000)
                    self.set_max_tries(10)
                    print("Difficulty level has been set to 'MEDIUM'")
                    break
                case "4":
                    self.difficulty = "HARD"
                    self.set_lower_bound(1)
                    self.set_higher_bound(10000)
                    self.set_max_tries(10)
                    print("Difficulty level has been set to 'HARD'")
                    break
                case default:
                    print("Please select a valid option. (1-3)")

            input("Press enter to go back to home screen")

    def change_difficulty(self):
        self.print_header("** Change Difficulty **", 40)
        self.set_difficulty()
        input("Press Enter to go back")

    def change_bounds(self):
        self.print_header("Change Highest And Lowest Number", 40)
        self.set_lower_bound()
        self.set_higher_bound()
        self.set_difficulty("CUSTOM")
        input("Press Enter to go back")

    def change_tries(self):
        self.print_header("Change maximum tries", size=40)
        self.set_max_tries()
        self.set_difficulty("CUSTOM")
        input("Press Enter to go back")

    def set_max_tries(self, tries=None):
        if tries:
            self.max_tries = tries
            return

        while True:
            print("Enter the maximum number of tries")
            response = input("> ")
            if response.isdecimal():
                self.max_tries = int(response)
                print(f"Maximum number of tries has been set to {self.max_tries}")
                break
            print("Please enter a valid number")

    def set_lower_bound(self, bound=None):
        if bound:
            self.lower_bound = bound
            return

        while True:
            print("Enter the lowest number I can pick")
            response = input("> ")
            if response.isdecimal():
                self.lower_bound = int(response)
                print(f"Lowest number has been set to {self.lower_bound}")
                break
            print("Please enter a valid number")

    def set_higher_bound(self, bound=None):
        if bound:
            self.higher_bound = bound
            return

        while True:
            print("Enter the highest number I can pick")
            response = input("> ")
            if response.isdecimal():
                self.higher_bound = int(response)
                print(f"Highest number has been set to {self.higher_bound}")
                break
            print("Please enter a valid number")

    def show_stats(self):
        self.print_header("Stats", 40)
        print(f"Matches Played: {self.matches}")
        print(f"Wins          : {self.wins}")
        print(f"Loses         : {self.matches - self.wins}")
        input("Press enter to go back.")

    def home(self):
        self.print_header("HOME", 20)
        print(f"1. Set Difficulty. {{ Current: {self.difficulty} }}")
        print(
            f"2. Set Lowest-Highest Number. {{ Current: {self.lower_bound} -  {self.higher_bound} }}"
        )
        print(f"3. Set Max Tries {{ Current: {self.max_tries} }}")
        print(f"4. Play")
        print(f"5. Show stats")
        print(f"Q. Quit")
        response = input("> ").upper()

        match response:
            case "1":
                self.change_difficulty()
            case "2":
                self.change_bounds()
            case "3":
                self.change_tries()
            case "4":
                self.play()
            case "5":
                self.show_stats()
            case "Q":
                print("Thanks For Playing! See you again!")
                input()

    def generate_number(self):
        return random.randint(self.lower_bound, self.higher_bound)

    def play(self):
        self.matches += 1
        print(
            f"I am thinking of a number between {self.lower_bound} to {self.higher_bound}"
        )
        number = self.generate_number()
        tries_left = self.max_tries
        tries = 0
        while tries_left > 0:
            print(f"You have {tries_left} tries left.")
            print("Enter your guess")
            response = input("> ")

            if not response.isdecimal():
                print("Please enter a valid guess. (Number)")
                continue

            response = int(response)
            tries += 1
            tries_left -= 1
            if response == number:
                print(f"You have successfully guessed the number in {tries} tries!")
                input(f"Congrats! Press Enter to continue!")
                self.wins += 1
                return

            if response < number:
                print(f"I am thinking of a bigger number :D")
                continue
            if response > number:
                print(f"I am thinking of a smaller number")
                continue

        print(f"I was thinking of {number}")
        print(f"You could not guess it. Better luck next time!")

    def run(self):
        while True:
            self.home()


if __name__ == "__main__":
    guess_the_number = GuessTheNumber()
    guess_the_number.run()

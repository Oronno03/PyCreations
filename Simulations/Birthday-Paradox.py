import datetime
import random


class BirthdayParadox:
    """
    The Birthday Paradox, also known as the Birthday Problem, refers to the high
    probability of at least two people sharing a birthday in a small group. For instance,
    in a group of 70 people, there's a 99.9% chance of a shared birthday. Even in a group
    as small as 23 people, there's a 50% chance. This program conducts Monte Carlo experiments
    to determine the probabilities for different group sizes.
    """

    def generate_birthdays(self, number_of_birthdays: int) -> list[datetime.date]:

        start_of_year = datetime.date(2001, 1, 1)

        return [
            start_of_year + datetime.timedelta(days=random.randint(0, 364))
            for _ in range(number_of_birthdays)
        ]

    def find_matching_birthday(self, birthdays: list[datetime.date]):

        if len(birthdays) == len(set(birthdays)):
            return None

        for index, birthday in enumerate(birthdays):
            for other_birthday in birthdays[index + 1 :]:
                if birthday == other_birthday:
                    return birthday

    def play(self):
        # Display the intro:
        print(
            """Birthday Paradox, 

        The Birthday Paradox shows us that in a group of N people, the odds
        that two of them have matching birthdays is surprisingly large.
        This program does a Monte Carlo simulation (that is, repeated random
        simulations) to explore this concept.

        (It's not actually a paradox, it's just a surprising result.)
        """
        )

        MONTHS = (
            "Jan",
            "Feb",
            "Mar",
            "Apr",
            "May",
            "Jun",
            "Jul",
            "Aug",
            "Sep",
            "Oct",
            "Nov",
            "Dec",
        )

        while True:
            print("How many birthdays do you want to generate? (Max 100)")
            response = input(">> ")

            if response.isdecimal():
                num_birthdays = min(100, max(1, int(response)))
                break

        print()

        print(f"Here are {num_birthdays} birthdays: ")
        birthdays = self.generate_birthdays(num_birthdays)
        for i, birthday in enumerate(birthdays):
            if i != 0:
                print(", ", end="")

            month_name = MONTHS[birthday.month - 1]
            print(f"{month_name} {birthday.day}", end="")

        print("\n")

        matching_birthday = self.find_matching_birthday(birthdays)

        print("In the simulation, ", end="")
        if matching_birthday is not None:
            month_name = MONTHS[matching_birthday.month - 1]
            print(
                f"Multiple people have birthday on {month_name} {matching_birthday.day}"
            )
        else:
            print("There are no matching birthdays")
        print()

        print(f"Generating {num_birthdays} random birthdays 100,000 times")
        input("Press any key to begin... ")
        print("Let's run another 100,000 simulations.")

        num_matches = 0
        for i in range(100_000):
            if i % 10_000 == 0:
                print(f"{i} simulation runs...")
            birthdays = self.generate_birthdays(num_birthdays)
            if self.find_matching_birthday(birthdays) is not None:
                num_matches += 1
        print("100,000 simulations run.")

        probability = round(num_matches / 100_000 * 100, 2)
        print(f"Out of 100,000 simulations of {num_birthdays} people, there was a")
        print(f"matching birthday in that group {num_matches} times. This means")
        print(f"that {num_birthdays} people have a {probability}% chance of having")
        print("a matching birthday in their group")
        print("That's probably more than what you would think.")


if __name__ == "__main__":
    bp = BirthdayParadox()
    bp.play()
    input()

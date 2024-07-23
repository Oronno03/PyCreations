import random


def roll():
    return random.randint(1, 6)


def get_players():
    players = {}
    while True:
        try:
            player_num = int(
                input("How many players do you want to play with? >> ")
            )
            break
        except ValueError:
            print("Please enter a valid amount")
            continue

    for i in range(player_num):
        print(f"Enter Player {i+1} name")
        name = input(">> ")
        players[name] = 0

    return players


def main():
    players = get_players()
    while max(players.values()) < 50:
        for player in players:
            print(f"\n{player}'s turn")
            print(f"{player}'s total point is: {players[player]}")
            curr_point = 0
            while True:
                print(f"{player}'s turn is going on")

                roll_now = input("Would you like to roll? ([y]/n) >> ").lower() != "n"

                if not roll_now:
                    break

                value = roll()

                if value == 1:
                    print("You rolled a 1. Your turn is over", end=" ")
                    print("Your current points won't be added")
                    curr_point = 0
                    break
                else:
                    curr_point += value
                    print(f"You rolled a {value}")
                    print(f"Your current point is: {curr_point}\n")
                input()
            players[player] += curr_point
            print(f"{player}'s total point is: {players[player]}")

    max_point = max(players.values())
    winners = [player for player, point in players.items() if point == max_point]
    if len(winners) > 1:
        print(f"Multiple players has the most points: {max_point}. They are: ")
        for i, player in enumerate(winners):
            print(f"{i+1}: {player}")
    else:
        print(f"{winners[0]} wins the game with a point of {max_point}")


def welcome():
    print("="*60)
    print("Welcome to PIG!".center(60))
    print("Play with as many players as you want.".center(60))
    print("** HOW TO PLAY **".center(60))
    print('''
How to Play?
- Each player gets to roll the dice
- Each time a player rolls a dice the number that gets on the dice is added to his point for that turn
- After rolling, a player can either choose to add the current turn's points to his total or roll again
- If he chooses to add his current turn's points, his points are added to the total and his turn ends
- But if he rolls a 1 before he adds his points to his total, his turn ends and his points aren't added
- Once a player has reached 50 or more points, that turn will be last turn for all the players.
- At the end of the turn for the last player, the player with the most point wins. Enjoy!
          ''')
    print("="*60)
    input("Press enter to continue!!")

try:
    welcome()
    print()
    main()
    input("Thanks for playing! See you again!")
except EOFError:
    input("You didn't complete the game.... Byeee!")

import random

teasers = [
    ("What has keys but can't open locks?", "keyboard"),
    ("What has a neck but no head?", "bottle"),
    ("What gets wetter as it dries?", "towel"),
    ("What has one eye but can't see?", "needle"),
    ("What comes down but never goes up?", "rain"),
    ("What has a heart that doesn't beat?", "artichoke"),
    ("What runs but never walks?", "river"),
    ("What can travel around the world while staying in a corner?", "stamp"),
    ("What has to be broken before you can use it?", "egg"),
    ("What has an end but no beginning?", "stick"),
    ("What has a face and two hands but no arms or legs?", "clock"),
    ("What is always in front of you but can't be seen?", "future"),
    ("What has a thumb and four fingers but is not a hand?", "glove"),
    ("What is so fragile that saying its name breaks it?", "silence"),
    (
        "What has cities, but no houses; forests, but no trees; and rivers, but no water?",
        "map",
    ),
    ("What can fill a room but takes up no space?", "light"),
    ("What has a head, a tail, but does not have a body?", "coin"),
    ("What gets broken without being held?", "promise"),
    ("What can you catch but not throw?", "cold"),
    ("What belongs to you, but other people use it more than you?", "name"),
    ("What has to be given before you can use it?", "permission"),
    ("What has one head, one foot, and four legs?", "bed"),
    (
        "What can run but never walks, has a mouth but never talks, has a head but never weeps, and has a bed but never sleeps?",
        "river",
    ),
    ("What can you keep after giving it to someone?", "word"),
    ("What has a bottom at the top?", "leg"),
    (
        "What comes once in a minute, twice in a moment, but never in a thousand years?",
        "m",
    ),
    ("What can you hold in your left hand but not in your right?", "right elbow"),
    ("What begins with T, ends with T, and has T in it?", "teapot"),
    ("What has four fingers and a thumb, but is not living?", "glove"),
    ("What has many teeth but can't bite?", "comb"),
    ("What has a tail but no body?", "coin"),
    ("What starts with 'e' and ends with 'e' but only has one letter?", "envelope"),
    (
        "What is as light as a feather, yet the strongest man can't hold it for more than five minutes?",
        "breath",
    ),
    ("What word is spelled incorrectly in every dictionary?", "incorrectly"),
    ("What has 88 keys but can't open a single door?", "piano"),
    ("What has hands but can't clap?", "clock"),
    ("What can be cracked, made, told, and played?", "joke"),
    ("What has feet but can't walk?", "ruler"),
    ("What has many keys but can't open a single lock?", "piano"),
    ("What has eyes but can't see?", "potato"),
    ("What comes up but never goes down?", "age"),
    ("What has space but no room?", "keyboard"),
    ("What has a ring but no finger?", "phone"),
    ("What is full of holes but still holds water?", "sponge"),
    (
        "What comes in different sizes, is more useful when it’s long, and when it's high, it can be seen from a great distance?",
        "shadow",
    ),
    (
        "What do you throw out when you want to use it but take in when you don't want to use it?",
        "anchor",
    ),
    ("What goes up and down but doesn't move?", "staircase"),
    ("What has no beginning, end, or middle?", "doughnut"),
    ("What has one horn and gives milk?", "milk truck"),
    ("What goes through towns and over hills but never moves?", "road"),
    ("What kind of coat can be put on only when wet?", "paint"),
    ("What has a bark but no bite?", "tree"),
    ("What has wings but can't fly?", "penguin"),
    ("What is red and smells like blue paint?", "red paint"),
    ("What comes in pairs but isn't socks?", "shoes"),
    ("What has a foot but no legs?", "ruler"),
    ("What is at the end of a rainbow?", "w"),
    ("What has 13 hearts but no organs?", "deck of cards"),
    ("What has a bank but no money?", "river"),
    ("What has a spine but no bones?", "book"),
    ("What is hard to find but easy to lose?", "trust"),
    ("What can fly without wings?", "time"),
    ("What has a lock but no key?", "hair"),
    ("What has a ring but no finger?", "phone"),
    ("What kind of tree can you carry in your hand?", "palm"),
]


def play_brain_teaser():
    random.shuffle(teasers)
    score = 0

    for question, answer in teasers:
        user_answer = input(question + " ").strip().lower()
        if user_answer == answer:
            score += 1
            print("Correct!\n")
        else:
            print(f"Wrong! The correct answer was: {answer}\n")

    print(f"Game Over! Your final score is: {score}/{len(teasers)}")


if __name__ == "__main__":
    play_brain_teaser()

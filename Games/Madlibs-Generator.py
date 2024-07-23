story = """
In the [adjective1] land of [place], a [animal] was feeling [emotion]. 
The [animal] had lost its [object].

Suddenly, a [character] appeared. 'I will help you find your [object],' they said.

Together, they journeyed through [terrain] and faced the [weather_condition]. 
Finally, they found the [object] in a [place2].
The [animal] was so [emotion2] and thanked the [character].
They lived [adverb] ever after.
"""

words = set()
start_of_word = -1

start = "["
end = "]"

for i, char in enumerate(story):
    if char == start:
        start_of_word = i

    if char == end and start_of_word != -1:
        word = story[start_of_word : i + 1]
        words.add(word)
        start_of_word = -1

answers = {}
for word in words:
    answer = input(f"Enter a word for {word}: ")
    answers[word] = answer


for word in words:
    story = story.replace(word, answers[word])

print(story)

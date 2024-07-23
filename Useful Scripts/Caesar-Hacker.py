import string
import sys

class CaesarHacker:
    def __init__(self):
        print("===============================")
        print("    Welcome to Caesar HACKER   ")
        print("===============================")
        input("Press enter to continue")
        self.set_characters()
        self.message = "Default Message"
        self.max_key = 93

    def run(self):
        while True:
            print("============")
            print("    HOME    ")
            print("============")
            print(f"1. Set The Encrypted Message {{ Current Message: {self.message} }}")
            print("2. Change Characters")
            print("3. Start Hacking")
            print("Q. Quit")
            response = input("> ").lower()

            match response:
                case "1":
                    self.set_message()
                case "2":
                    self.set_characters()
                case "3":
                    hacked_messages = self.hack()
                    for key, message in hacked_messages.items():
                        print(f"Key {key}: {message}")
                case "q":
                    print("="*40)
                    print("Thanks for using this program!".center(40))
                    print("="*40)
                    sys.exit()

    def hack(self):
        hacked = {}
        for key in range(self.max_key+1):
            decrypted = ""

            for i, char in enumerate(self.message):
                if not char in self.characters:
                    decrypted += char
                    continue

                shifted_index = (self.characters.index(char) - i - key) % len(self.characters)
                decrypted += self.characters[shifted_index]

            hacked[key] = decrypted
        return hacked
            

    def set_message(self):
        print("==============================")
        print("   Set The Encrypted Message  ")
        print("==============================")
        print(f"Enter the message to hack")
        self.message = input("> ")

    def set_characters(self):
        print("================================")
        print("         Set Characters         ")
        print("================================")
        self.characters = ""

        print("When choosing the characters, make sure that each type of character")
        print("you set is actually encrypted in the actual message and it isn't just")
        print("directly added. If you aren't sure which type of characters are encrypted.")
        print("Try using different combinations until you get a meaningful message.")
        input("Press enter to continue:")

        possible_characters = {
            "lowercase": string.ascii_lowercase,
            "uppercase": string.ascii_uppercase,
            "digits": string.digits,
            "punctuations": string.punctuation,
        }

        for character_type, characters in possible_characters.items():
            print(f"Does your message have {character_type} (encrypted) in it? ([y]/n)")
            response = input("> ")
            if response.lower() != 'n':
                self.characters += characters
                print(f"Added {character_type}!")
                continue
            print(f"Skipping {character_type}")

if __name__ == '__main__':
    ch = CaesarHacker()
    ch.run()
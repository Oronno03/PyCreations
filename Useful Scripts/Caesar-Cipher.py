import string
import sys

class CaesarCipher:
    def __init__(self):
        print("==========================")
        print(" Welcome to Caesar Cipher ")
        print("==========================")
        input("Press enter to continue")
        self.set_characters()
        self.mode = "encrypt"
        self.key = 3
        self.message = "Default Message."

    def run(self):
        while True:
            print("============")
            print("    HOME    ")
            print("============")
            print(f"1. Choose Mode. {{ Current Mode: {self.mode} }}")
            print(f"2. Set Key. {{ Current Key: {self.key} }}")
            print(f"3. Set message. {{ Current Message: {self.message[:50]} }}")
            print("4. HELP")
            print("5. Change Characters")
            print(f"6. Start {self.mode}ing")
            print("Q. Quit")
            response = input("> ").lower()

            match response:
                case "1":
                    self.set_mode()
                case "2":
                    self.set_key()
                case "3":
                    self.set_message()
                case "4":
                    self.get_help()
                case "5":
                    self.set_characters()
                case "6":
                    self.start()
                case "q":
                    print("="*40)
                    print("Thanks for using this program!".center(40))
                    print("="*40)
                    sys.exit()
                case default:
                    print("Please choose a valid option. (1-6) or Q to quit")

    def set_characters(self):
        print("================================")
        print("         Set Characters         ")
        print("================================")
        self.characters = ""

        possible_characters = {
            "lowercase": string.ascii_lowercase,
            "uppercase": string.ascii_uppercase,
            "digits": string.digits,
            "punctuations": string.punctuation,
        }

        for character_type, characters in possible_characters.items():
            print(f"Will you have {character_type} in your message? ([y]/n)")
            response = input("> ")
            if response.lower() != 'n':
                self.characters += characters
                print(f"Added {character_type}!")
                continue
            print(f"Skipping {character_type}")

    def start(self):
        match self.mode:
            case "encrypt":
                print("Encrypting...")
                result = self.encrypt()
                print(f"Encrypted Message: {result}\nEncrypted with key: {self.key}")
            case 'decrypt':
                print("Decrypting...")
                result = self.decrypt()
                print(f"Decrypted Message: {result}\nDecrypted with key: {self.key}")
            case default:
                print("Something went wrong. Please recheck the mode.")
        input("")

    def get_help(self):
        print("============")
        print("    HELP    ")
        print("============")
        print("* To encrypt a message, from the home menu select 1 then from the modes menu select 'e'")
        print("     > When encrypting, a message will be shifted forward by the key")
        print("* To decrypt a message, from the home menu select 1 then from the modes menu select 'd'")
        print("     > When decrypting, a message will be shifted backward by the key")
        print("* To set a key, (default = 3), from the home menu select 2 and then type the key")
        print("     > The key is the amount by which the characters are shifted during encryption or decryption")
        print("* To set a message, from the home menu select 3 and then type the message")
        print("     > It is the message you want to encrypt or decrypt")
        print("* To start encrypting or decrypting, from the home menu select 5")
        print("     > Make sure you have the correct mode, key and message set as per what you want")
        input()

    def set_mode(self):
        print("==============================")
        print("          Set Mode            ")
        print("==============================")
        while True:
            print("Do you want to Encrypt (e) or Decrypt (d)?")
            response = input("> ")

            match response:
                case "e":
                    self.mode = "encrypt"
                case "d":
                    self.mode = "decrypt"
                case default:
                    print("Please enter a valid response, (e|d).")
                    continue
            break

    def set_key(self):
        print("==============================")
        print("           Set KEY            ")
        print("==============================")
        while True:
            max_key = len(self.characters) - 1
            print(f"Please enter the key (0-{max_key}) to use")
            response = input("> ")

            if response.isdecimal() and 0 <= int(response) <= max_key:
                self.key = int(response)
                break

            print(f"Please enter a valid numeric key from 0 to {max_key}")

    def set_message(self):
        print("==============================")
        print("         Set Message          ")
        print("==============================")
        print(f"Enter the message to {self.mode}")
        self.message = input("> ")

    def encrypt(self):
        encrypted = ""
        for i, char in enumerate(self.message):
            if not char in self.characters:
                encrypted += char
                continue

            shifted_index = (self.characters.index(char) + i + self.key) % len(self.characters)
            encrypted += self.characters[shifted_index]

        return encrypted

    def decrypt(self):
        decrypted = ""
        for i, char in enumerate(self.message):
            if not char in self.characters:
                decrypted += char
                continue

            shifted_index = (self.characters.index(char) - i - self.key) % len(self.characters)
            decrypted += self.characters[shifted_index]

        return decrypted

if __name__ == '__main__':
    cc = CaesarCipher()
    cc.run()

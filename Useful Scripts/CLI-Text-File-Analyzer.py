import os
import re
from collections import Counter

class TextFileAnalyzer:
    def __init__(self, filepath, encoding='utf-8'):
        self.filepath = filepath
        self.encoding = encoding
        self.text = self._read_file()

    def _read_file(self):
        with open(self.filepath, "r", encoding=self.encoding) as file:
            return file.read()
        
    def word_count(self):
        words = re.findall(r"\b\w+\b", self.text.lower())
        return len(words)
    
    def line_count(self):
        lines = self.text.split("\n")
        return len(lines)
    
    def char_count(self, include_space=True):
        if include_space:
            return len(self.text)
        else:
            return len(self.text.replace(" ", ""))
        
    def most_frequent_words(self, n=10):
        words = re.findall(r'\b\w+\b', self.text.lower())
        word_counts = Counter(words)
        return word_counts.most_common(n)
    
    def sentence_count(self):
        sentences = re.split(r'[.!?]+', self.text)
        return len(sentences) - 1
    
    def eta_reading_time(self, words_per_minute=200):
        word_count = self.word_count()
        return f"{round(word_count / words_per_minute, 2)} minutes"
    
    def get_statistics(self):
        stats = {
            "Word Count": self.word_count(),
            "Line Count": self.line_count(),
            "Character Count (With Spaces)": self.char_count(),
            "Character Count (Without Spaces)": self.char_count(include_space=False),
            "Most Frequent Words (Top 10)": self.most_frequent_words(), 
            "Sentence Count": self.sentence_count(),
            "Estimated Reading Time (200 WPM)": self.eta_reading_time()
        }
        return stats

class TextFileAnalyzerApp:
    def __init__(self):
        self.analyzer = None
    
    def load_file(self):
        while True:
            print("Enter the path to the text file. Q to exit.")
            filepath = input(">")
            if filepath.upper() == "Q":
                print("Goodbye!")
                quit()
            if os.path.exists(filepath) and os.path.isfile(filepath):
                self.analyzer = TextFileAnalyzer(filepath)
                print(f"File '{filepath}' loaded successfully!")
                return
            print("File not found. Please enter a valid file path!")

    def run(self):
        self.load_file()
        
        if not self.analyzer:
            print("Something wrong happened please rerun the program")
            quit()

        while True:
            print("\nText File Analyzer")
            print("1. Word Count")
            print("2. Line Count")
            print("3. Character Count (with spaces)")
            print("4. Character Count (without spaces)")
            print("5. Most Frequent Words")
            print("6. Sentence Count")
            print("7. Estimated Reading Time")
            print("8. Full Statistics")
            print("9. Change File")
            print("Q. Quit")
            choice = input("Select an option: ").strip().upper()

            match choice:
                case "1":
                    print(f"Total Words: {self.analyzer.word_count()}")
                    input("Press Enter to return to the menu.")
                case "2":
                    print(f"Total Lines: {self.analyzer.line_count()}")
                    input("Press Enter to return to the menu.")
                case "3":
                    print(f"Total Characters (With Spaces): {self.analyzer.char_count()}")
                    input("Press Enter to return to the menu.")
                case "4":
                    print(f"Total Characters (Without Spaces): {self.analyzer.char_count(include_space=False)}")
                    input("Press Enter to return to the menu.")
                case "5":
                    while True:
                        print("Enter top N most frequent words you want to see. Default is 10.")
                        n = input("> ")
                        if n and not n.isdecimal():
                            print("Please enter a valid number.")
                            continue
                        n = int(n) if n else 10
                        break
                    print(f"Most Frequent Words (Top {n}):")
                    words = self.analyzer.most_frequent_words()
                    print("Word: Count")
                    for word, count in words:
                        print(f"{word}: {count}")
                    input("Press Enter to return to the menu.")
                case "6":
                    print(f"Total Sentences: {self.analyzer.sentence_count()}")
                    input("Press Enter to return to the menu.")
                case "7":
                    while True:
                        print("Enter your reading speed (WPM). Default is 200.")
                        speed = input("> ")
                        if speed and not speed.isdecimal():
                            print("Please enter a valid speed (number).")
                            continue
                        speed = int(speed) if speed else 200
                        break
                    print(f"Estimated Reading Time (at {speed} WPM): {self.analyzer.eta_reading_time(speed)}")
                    input("Press Enter to return to the menu.")
                case "8":
                    print("\n" + "="*50)
                    print(f"STATISTICS FOR {self.analyzer.filepath}")
                    full_stats = self.analyzer.get_statistics()
                    for key, value in full_stats.items():
                        print(f"{key}: {value}")
                    print("="*50 + "\n")
                    input("Press Enter to return to the menu.")
                case "9":
                    self.load_file()
                    input("Press Enter to return to the menu.")
                case "Q":
                    print("Goodbye!")
                    break
                case _:
                    print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    app = TextFileAnalyzerApp()
    try:
        app.run()
    except:
        print("Quitting")

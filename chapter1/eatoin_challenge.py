"""Challenge etaion."""
from collections import defaultdict
import pprint

def main():
    """Map characters to dictionary and output in bar-chart type display."""
    while True:
        text = input("Please enter a text in Spanish: ")
        while (len(text) == 0):
            print()
            text = input("Please enter a text in Spanish: ")
        bchart = defaultdict(list)
        for char in text:
            char = char.lower()
            if char.isalpha():
                bchart[char].append(char)
        pprint.pprint(bchart)
        try_again = input("\nTry again? (Press Enter else n to quit)\n ")
        if try_again.lower() == "n":
            break

if __name__ == "__main__":
    main()

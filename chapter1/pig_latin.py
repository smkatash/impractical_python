"""Turn a word into its Pig Latin equivalent."""

def main():
    """Convert input into pig latin."""
    vowel = "aeiouy"
    while True:
        word = input("Please enter a word: ")
        if word[0].lower() in vowel:
            word += "way"
        else:
            word = word[1:] + word[0] + "ay"
        print("Pig latin: ", word)
        try_again = input("\nTry again? (Press Enter else n to quit)\n ")
        if try_again.lower() == "n":
            break

if __name__ == "__main__":
    main()

"""Identify if word is a palindrome"""
def is_palindrome(word):
    """Recursively check if first and last letter are equal"""
    if len(word) > 1:
        if word[0] == word[-1]:
            word = word[1:-1]
            return is_palindrome(word)
        else:
            return False
    else:
        return True


def main():
    word = "racecar"
    print(is_palindrome(word))

if __name__ == "__main__":
    main()
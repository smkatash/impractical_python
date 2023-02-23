
def main():
    word = "nurses run"
    word1 = "nur sesrun"
    pali_list = []
    l = len(word)
    reversed_word = word[::-1]
    if l > 1:
        for i in range(l):
            if word[i:] == reversed_word[:l-i] and reversed_word[l-i:] == word1:
                pali_list.append((word, reversed_word[l-i:]))
            if word[:i] == reversed_word[l-i:] and reversed_word[:l-i] == word1:
                pali_list.append((reversed_word[:l-i], word))
    palingrams = sorted(pali_list)
    print("\nNumber of palingrams = {}\n".format(len(palingrams)))
    for first, second in palingrams:
        print("{} {}".format(first, second))

if __name__ == "__main__":
    main()
"""Find letter palingrams in a dictionary file."""
from load_dictionary import load

def get_palingrams():
    words_list = load('dictionary.txt')
    pali_list = []
    for word in words_list:
        l = len(word)
        reversed_word = word[::-1]
        if l > 1:
            for i in range(l):
                if word[i:] == reversed_word[:l-i] and reversed_word[l-i:] in words_list:
                    pali_list.append((word, reversed_word[l-i:]))
                if word[:i] == reversed_word[l-i:] and reversed_word[:l-i] in words_list:
                    pali_list.append((reversed_word[:l-i], word))
    palingrams = sorted(pali_list)
    print("\nNumber of palingrams = {}\n".format(len(palingrams)))
    return pali_list
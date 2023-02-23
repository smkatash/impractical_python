"""Find palindromes (letter palingrams) in a dictionary file."""
from load_dictionary import load

def get_palindromes():
    words_list = load('/usr/share/dict/words')
    pali_list = []
    for word in words_list:
        if len(word) > 1 and word == word[::-1]:
            pali_list.append(word)
    print("\nNumber of palindromes found = {}\n".format(len(pali_list)))
    return pali_list

"""Find palingrams in a dictionary file."""
from load_dictionary import load

def find_palingrams():
    pali_list = []
    words_set = set(load('dictionary.txt'))
    for word in words_set:
        end = len(word)
        rev_word = word[::-1]
        if end > 1:
            for i in range(end):
                if word[i:] == rev_word[:end-i] and rev_word[end-i:] in words_set:
                    pali_list.append((word, rev_word[end-i:]))
                if word[:i] == rev_word[end-i:] and rev_word[:end-i] in words_set:
                    pali_list.append((rev_word[:end-i], word))
    return pali_list

def main():
    print(find_palingrams())
    

if __name__ == "__main__":
    main()
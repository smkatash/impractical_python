"""Load a file as a list"""
import sys

def load(file):
    """Open a file and return a list of string"""
    try:
        with open(file) as infile:
            word_list = infile.read().strip().split('\n')
            word_list = [word.lower() for word in word_list]
            return word_list
    except IOError as e:
        print("{}\nError opening {}. Terminating program.".format(e, file), file=sys.stderr)
        sys.exit(1)

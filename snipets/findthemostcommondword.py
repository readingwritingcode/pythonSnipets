#!/usr/bin/python3

import re
from colelctions import Counter

def most_common_words('path_to_txt',num_of_common_word=10):

    words = re.findall(r'\w+',open('path_to_text').read().lower())
    mostcw = Counter(words).most_common(num_of_common_word)
    print(mostcw)
    return mostcw

def main():
    path_to_txt = input('insert path to text')
    most_common_words(path_to_txt)

if __name__ == "__main__":
    main()

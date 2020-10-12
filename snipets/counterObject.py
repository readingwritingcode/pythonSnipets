#!/usr/bin/python3

from collections import Counter

cnt = Counter()

def counterObject():

    for word in ['red', 'blue', 'green', 'blue', 'blue']:
        cnt[word] += 1
    print(dict(cnt))
    return cnt

def main():
    counterObject()

if __name__ == "__main__":
    main()
    

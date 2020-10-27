#!/usr/bin/python3

'''this method return the most frequent element that apears
in a list'''

def most_frequent(list):
    _max = max(set(list),key = list.count)
    print(_max)
    return _max

if __name__ == "__main__":
    numbers = [1,2,3,2,5,6,1,4]
    most_frequent(numbers)

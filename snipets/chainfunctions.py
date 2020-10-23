#!/usr/bin/python3

'''chain multiple functions in one line'''

def add(a,b):
    return a + b

def subtract(a,b):
    return a - b

if __name__ == "__main__":
    a,b = 4,5
    print((subtract if a > b else add)(a,b))

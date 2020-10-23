#!/usr/bin/python3

'''the following method can be user to merge two dicts'''

def merge_two_dicts(a,b):
    c = a.copy()
    c.update(b)
    return c

if __name__ == "__main__":
    a = {'x':1, 'y':2}
    b = {'y':3,'z':4}
    assert merge_two_dicts(a,b) == {'x':1,'y':3,'z':4}

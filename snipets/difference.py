#!/usr/bin/python3

'''
the following finds the difference between two iterables by keeping only the
values that are in the firts one.
'''

def difference(a, b):
    set_a = set(a)
    set_b = set(b)
    comparison = set_a.difference(set_b)
    print(comparison)
    return list(comparison)

if __name__ == "__main__":
    a = [1,2,3,4]
    b = [1,2,3,]

    assert difference(a,b) == [4]
    

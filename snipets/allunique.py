#!/usr/bin/python3

'''all unique elements from a list of elements'''

def all_unique(list):
    return len(list) == len(set(list))

if __name__ == "__main__":

    '''test'''
    x = [1,1,1,2,2,2,3,3,3]
    y = [1,2,3]

    assert all_unique(x) == False
    assert all_unique(y) == True

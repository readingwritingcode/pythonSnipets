#!/usr/bin/python3

'''check wheter a list has duplicated values by using the fact that set()
   contains only unique elements'''

def has_duplicates(lst):
    return len(lst) != len(set(lst))

if __name__ == "__main__":
    x = [1,2,3,4]
    y = [1,2,3,4,4,5,5]
    assert has_duplicates(x) == False
    assert has_duplicates(y) == True

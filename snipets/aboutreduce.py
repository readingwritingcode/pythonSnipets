#!/usr/bin/python3

'''reduce is a really usefull function for performing some computation on a list
   and returning the result. It applies a rolling computation to sequencial
   pairs of values in a list.for example, multiply a elements in a list.
'''

from functools import reduce

def multiply_elements_list(list_of_elements):
    rslt = reduce((lambda x,y:x*y), list_of_elements)
    print(rslt)
    return rslt

if __name__ == "__main__":
    _list=[1,2,3]
    assert multiply_elements_list(_list) == 6
    

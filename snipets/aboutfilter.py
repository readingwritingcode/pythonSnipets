#!/usr/bin/python3

'''filter creates a list of elements for which a function returns true.'''

def  less_than_zero(list_of_elements):
    rslt= list(filter(lambda x:x<0,list_of_elements))
    print(rslt)
    return rslt

if __name__ == "__main__":

    _list = range(-5,5)
    assert less_than_zero(_list) == [-5,-4,-3,-2,-1]

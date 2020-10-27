#!/usr/bin/python3

'''convert list, to dicts'''

# my way

def list_to_dict(list_one,list_two):
    _dict ={}

    for i in range(len(list_one)):
        _dict[list_one[i]] = list_two[i]

    return _dict

#pythonic way

def to_dictionary(keys,values):
    return dict(zip(keys,values))

if __name__ == "__main__":
    list_one = ['a','b','c']
    list_two = [1,2,3]

    assert to_dictionary(list_one,list_two) == list_to_dict(list_one,list_two)

    

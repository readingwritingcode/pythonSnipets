#!/usr/bin/python3

'''map applies a function to all the items in an input_list.
   blueprint: map(function_to_apply, list_of_inputs)
'''

def squared(list_of_inputs):
    rslt = list(map(lambda x:x**2,list_of_inputs))
    print(rslt)
    return rslt

if __name__ == "__main__":

    _list = [2, 4, 8]

    assert squared(_list) == [4, 16, 64]

#!/usr/bin/python3

''' the following methods flatten a potentially deep list using recursion.
'''

def spread(arg):
    ret = []
    for i in arg:
        if isinstance(i,list):
            ret.extend(i)
        else:
            ret.append(i)
    return ret

def deep_flatten(xs):
    flat_list = []
    print(xs)
    rslt = [flat_list.extend(deep_flatten(x)) for x in xs] if isinstance(xs,list) else flat_list.append(xs)
    return rslt
'''bug here'''
if __name__ =="__main__":
    _list = [1, [2],[[3],4], 5]
    assert deep_flatten(_list) == [1, 2, 3, 4, 5]
    

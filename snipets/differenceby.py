#!/usr/bin/python3

'''the following  returns the difference between two list after appliying
   a given function to each element of both list.
'''

from math import floor

def difference_by(a,b,fn):
    b = set(map(fn,b))
    return [item for item in a if fn(item) not in b]

if __name__ == '__main__':
    assert difference_by([2.1,1.2],[2.3,3.4],floor) == [1.2]
    assert difference_by([{'x':2},{'x':1}], [{'x':1}], lambda v:v['x'])

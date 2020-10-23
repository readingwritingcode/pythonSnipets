#!/usr/bin/python3

'''sum list of dicts. prove several methods'''

#method one

from collections import Counter
from functools import reduce

def sum_list_of_dicts(lst_dcts):
    counter = Counter()
    for d in lst_dcts:
        counter.update(d)
    return counter

#method two
def sum_list_of_dicts_m2(dct):
    dictf = reduce(lambda x,y:dict((k,v+y[k]) for k,v in x.items()),dct)
    return dictf

if __name__ == "__main__":
    #method one
    lst_dct = [{'a':10,'b':12},{'a':14,'b':15}]
    print(sum_list_of_dicts(lst_dct))

    assert sum_list_of_dicts_m2(lst_dct) == sum_list_of_dicts(lst_dct)

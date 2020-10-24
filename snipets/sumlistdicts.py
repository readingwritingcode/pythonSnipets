#!/usr/bin/python3

'''sum list of dicts. prove several methods'''

from collections import Counter

#method one Counter util
def fCounter(dictList):
    c = Counter()
    for d in dictList:
        c.update(d)
    return c

#method two
def fReduce(dictList):
    return reduce(
        lambda x,y:{
            k: x[k] + y[k]
            for k in dictList[0].iterkeys()
            },
            dictList
            )

#method three
def fSum(dictList):
    return (
        {k:sum(d[k] for d in dictList) for k in dictList[0]
         )
if __name__ =="__main__":
        pass

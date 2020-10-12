#!/usr/bin/python3

import sys

def check_memory_bites(thing):
    print('size of object is:', sys.getsizeof(thing))

def check_memory_bytes(thing):
    print('size of object in bytes is:', sys.getsizeof(thing)/8)
    

if __name__ == "__main__":

    thing = [x for x in  range(1000)]

    check_memory_bites(thing)

    check_memory_bytes(thing)

#!/usr/bin/python3

''' this snippet can be use to calculate the time it takes to
    to execute a particular code'''

import time

start_time = time.time()
a = 1
b = 2
c = a + b
print(c)

end_time = time.time()
total_time = end_time - start_time

print("total time", total_time)

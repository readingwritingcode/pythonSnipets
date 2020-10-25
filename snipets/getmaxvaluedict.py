#/usr/bin/python3

'''
get max value from a dict with a lot of key-value pairs
'''

# most eficient aproach. build this test!!!

def key_with_max_value(_dict):

    v = list(_dic.values()) # list of values from dict
    k = list(_dic.values()) # list of keys from dict
    key_with_max_value = k[v.index(max(v))]

    return key_wit_max_value

# below some other candidate methods and test performance
# https://stackoverflow.com/questions/268272/getting-key-with-maximum-value-in-dictionary


#!/usr/bin/python3

import operator

action = {
    "+": operator.add,
    "-": operator.sub,
    "/": operator.truediv,
    "*": operator.mul,
    "**":operator.pow
    }

print(action['**'](2,2))

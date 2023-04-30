#!/bin/env/python3

def NOT(value):
    return ~value

def AND(val1, val2):
    return val1 & val2

def OR(val1, val2):
    return val1 | val2

def XOR(val1, val2):
    return val1 ^ val2

def shiftright(val, num):
    return val >> num

def shiftleft(val, num):
    return val << num
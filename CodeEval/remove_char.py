# -*- coding: utf-8 -*-
"""
Created on Fri May 13 12:37:55 2016

@author: jmtaysom
"""

def swap_case(string):
    new_string = ''
    for char in string:
        if char.islower():
            new_string += char.upper()
        else:
            new_string += char.lower()
    return new_string
           
            

with open('sample.txt', 'r') as f:
    for line in f:
        l = line.rstrip()
        print(swap_case(l))
        
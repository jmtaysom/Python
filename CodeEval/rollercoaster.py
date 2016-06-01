# -*- coding: utf-8 -*-
"""
Created on Fri May 13 12:37:55 2016

@author: jmtaysom
"""
import sys

def rollercoaster(string):
    new_string = ''
    upper = True
    for char in string:
        if char.isalpha() and upper:
            new_string += char.upper()
            upper = False
        elif char.isalpha():
            new_string += char.lower()
            upper = True
        else:
            new_string += char
            
    return new_string
           
            

with open('sample.txt', 'r') as f:
    for line in f:
        l = line.rstrip()
        print(rollercoaster(l))
        
sys.exit()
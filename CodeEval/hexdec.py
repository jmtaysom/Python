# -*- coding: utf-8 -*-
"""
Created on Fri May 13 12:37:55 2016

@author: jmtaysom
"""
lut = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5,'6':6, '7':7, '8':8,
       '9':9, 'a':10, 'b':11, 'c':12, 'd':13, 'e':14, 'f':15}

def hexidecimal(h):
    total = 0    
    h_reverse = h[::-1]
    for i, n in enumerate(h_reverse):
        value = lut[n] * 16**i
        total += value
    return total
           
            

with open('sample.txt', 'r') as f:
    for line in f:
        l = line[:-1]
        print(hexidecimal(l))
        
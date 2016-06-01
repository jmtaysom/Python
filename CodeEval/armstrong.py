# -*- coding: utf-8 -*-
"""
Created on Fri May 13 12:37:55 2016

@author: jmtaysom
"""

def armstrong(s):
    total = 0
    n = int(s)
    length = len(s)
    for c in s:
        c = int(c)
        total += c**length
    return total == n
           
            

with open('sample.txt', 'r') as f:
    for line in f:
        l = line.rstrip()
        print(armstrong(l))
        
# -*- coding: utf-8 -*-
"""
Created on Fri May 13 12:37:55 2016

@author: jmtaysom
"""
import sys

def pop_print(lst):
    if len(lst) % 2 == 0:
        lst = lst[-1::-2]
    else:
        lst = lst[::-2]
    return ' '.join(lst)
            

with open('sample.txt', 'r') as f:
    for l in f:
        if l != '\n':        
            l = l.rstrip()
            l = l.split(' ')
            print(pop_print(l))
        
sys.exit()
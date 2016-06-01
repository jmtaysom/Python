# -*- coding: utf-8 -*-
"""
Created on Fri May 13 12:37:55 2016

@author: jmtaysom
"""
import sys.argv
import sys.exit

alpha = 'abcdefghijklmnopqrstuvwxyz'
alpha = set([c for c in alpha])

def pangram(lst):
    out = list(alpha-lst)
    out.sort()
    out = ''.join(out)
    if out == '':
        out = 'NULL'
    return out
            

with open('sample.txt', 'r') as f:
    for l in f:
        if l != '\n':        
            l = l.rstrip()
            l = set([c.lower() for c in l])
            print(pangram(l))
        
sys.exit()
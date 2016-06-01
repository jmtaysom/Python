# -*- coding: utf-8 -*-
"""
Created on Fri May 13 12:37:55 2016

@author: jmtaysom
"""
import sys

def cap(string):
    out = []
    words = string.split(' ')
    for word in words:
        o = word[0].capitalize()  
        o += word[1:]
        out.append(o)
    return ' '.join(out)
            

with open('sample.txt', 'r') as f:
    for line in f:
        if line != '\n':        
            l = line.rstrip()
            print(cap(l))
        
sys.exit()
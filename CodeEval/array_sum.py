# -*- coding: utf-8 -*-
"""
Created on Fri May 13 12:37:55 2016

@author: jmtaysom
"""
import sys

def array_sum(series):
    final = -99999999999
    for i, start in enumerate(series):
        if start > final:
            final = start
        total = 0
        for x in series[i:]:
            total += x
            if total > final:
                final = total
            
    return final
            

with open('sample.txt', 'r') as f:
    for l in f:
        if l != '\n':        
            l = l.rstrip()
            l = l.split(',')
            l = [int(x) for x in l]
            print(array_sum(l))
        
sys.exit()
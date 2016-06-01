# -*- coding: utf-8 -*-
"""
Created on Fri May 13 12:37:55 2016

@author: jmtaysom
"""

with open('sample.txt', 'r') as f:
    for line in f:
        x,n = [int(i) for i in line.split(',')]
        inc = n        
        while n <= x:
            n+=inc
        print(n)
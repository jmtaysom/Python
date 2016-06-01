# -*- coding: utf-8 -*-
"""
Created on Fri May 13 12:37:55 2016

@author: jmtaysom
"""


with open('sample.txt', 'r') as f:
    for line in f:
        a = set(line.split(',')[:-1])
        b = list(a)
        b.sort()
        print(','.join(b))
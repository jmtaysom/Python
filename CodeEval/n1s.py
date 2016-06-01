# -*- coding: utf-8 -*-
"""
Created on Fri May 13 12:37:55 2016

@author: jmtaysom
"""
import sys
from math import sqrt

def distance(x1,y1,x2,y2):
    d = sqrt((x2-x1)**2 + (y2-y1)**2)
    return int(d)
           
            

with open('sample.txt', 'r') as f:
    for line in f:
        l = line.rstrip()
        l = l.strip('())')
        c1, c2 = l.split(') (')
        x1, y1 = c1.split(', ')
        x2, y2 = c2.split(', ')
        x1 = int(x1)
        x2 = int(x2)
        y1 = int(y1)
        y2 = int(y2)
        print(distance(x1,y1,x2,y2))
        
sys.exit()
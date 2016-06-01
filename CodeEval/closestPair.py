# -*- coding: utf-8 -*-
"""
Created on Fri May 13 12:37:55 2016

@author: jmtaysom
"""
import sys
from math import sqrt

def distance(x1,y1,x2,y2):
    d = sqrt((x2-x1)**2 + (y2-y1)**2)
    return d

def coordinate(string):
    x, y = string.split(' ')
    x = int(x)
    y = int(y)
    return (x,y)

with open('sample.txt', 'r') as f:
    coor_list = []
    dist = 10000
    for line in f:
        
        l = line.rstrip()
        if ' ' in l:
            coor = coordinate(l)
            coor_list.append(coor)
            if len(coor_list) > 1:
                for c in coor_list:
                    d = distance(coor[0],coor[1],*c)
                    
                    if d < dist and d>0:
                        dist = d
            
        elif l == '0':
            if dist < 10000:            
                print('{:.4f}'.format(dist))
            else:
                print('INFINITY')
            coor_list = []            
            dist = 10000
            
            
        
#sys.exit()
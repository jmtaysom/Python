# -*- coding: utf-8 -*-
"""
Created on Fri May 13 12:37:55 2016

@author: jmtaysom
"""


with open('sample.txt', 'r') as f:
    for line in f:
        n,p1,p2 = [int(i) for i in line.split(',')]
        b = '{0:b}'.format(n)      
        if b[-1*p1] == b[-1*p2]:
            print('true')
        else:
            print('false')
# -*- coding: utf-8 -*-
"""
Created on Fri May 13 08:19:30 2016

@author: jmtaysom
"""

with open('SampleEndsWith.txt','r') as f:
    for line in f:
        sample,end = line.split(',')
        if sample.endswith(end[:-1]):
            print(1)
        else:
            print(0)
        
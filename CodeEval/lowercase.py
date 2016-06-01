# -*- coding: utf-8 -*-
"""
Created on Fri May 13 12:37:55 2016

@author: jmtaysom
"""

with open('sample.txt', 'r') as f:
    for line in f:
        print(line[:-1].lower())
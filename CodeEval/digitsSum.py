# -*- coding: utf-8 -*-
"""
Created on Fri May 13 11:58:52 2016

@author: jmtaysom
"""
import sys

with open('digitsSum.txt', 'r') as f:
    for line in f:
        print(sum((int(char) for char in line[:-1])))
        
sys.exit()
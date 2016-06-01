# -*- coding: utf-8 -*-
"""
Created on Fri May 13 09:08:17 2016

@author: jmtaysom
"""
import sys

with open('mth.txt', 'r') as f:
    for line in f:
        sample = line.split()[:-1]
        n = int(line.split()[-1])
        if n <= len(sample):        
            print(sample[n*-1])
            
sys.exit()
        
        
# -*- coding: utf-8 -*-
"""
Created on Fri May 13 12:37:55 2016

@author: jmtaysom
"""
import sys

def num_sort(string):
    new_s = ''
    nums = string.split(' ')
    nums = [float(x) for x in nums]
    nums.sort()    
    for x in nums:
        s = '{:.3f} '.format(x)
        new_s += s
    new_s = new_s.rstrip()
    return new_s
           
            

with open('sample.txt', 'r') as f:
    for line in f:
        if line != '\n':        
            l = line.rstrip()
            
            print(num_sort(l))
        
sys.exit()
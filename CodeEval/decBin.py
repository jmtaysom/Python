# -*- coding: utf-8 -*-
"""
Created on Fri May 13 12:37:55 2016

@author: jmtaysom
"""
import sys


def dec_bin(string):
    b = '{:b}'.format(int(string))
    return b
           
            

with open('sample.txt', 'r') as f:
    for line in f:
        if line != '\n':        
            l = line.rstrip()
            chars,keys = l.split('|')
            keys = keys.lstrip()
            keys = keys.split(' ')            
            print(keys)
            #print(dec_bin(l))
        
sys.exit()
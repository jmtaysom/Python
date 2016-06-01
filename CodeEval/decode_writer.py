# -*- coding: utf-8 -*-
"""
Created on Fri May 13 12:37:55 2016

@author: jmtaysom
"""
import sys

def decode(string,keys):
    new_s = ''
    for key in keys:
        new_s += string[key]
    return new_s
           
            

with open('sample.txt', 'r') as f:
    for line in f:
        if line != '\n':        
            l = line.rstrip()
            chars,keys = l.split('|')
            keys = keys.lstrip()
            keys = keys.split(' ')
            keys = [int(key)-1 for key in keys]
            #print(keys)
            print(decode(chars,keys))
        
sys.exit()
# -*- coding: utf-8 -*-
"""
Created on Mon May 23 20:47:45 2016

@author: jmtaysom
"""

import sys

def read_more(string):
    if len(string) < 56:
        return string
    else:
        string = string[:40]
        if ' ' in string:
            stringl = string.split(' ')
            stringl.pop()
            string = ' '.join(stringl)
        string += '... <Read More>'
        return string
        
with open('sample.txt' ,'r') as f:
    for l in f:
        l = l.rstrip()
        if l != '':
            print(read_more(l))
            
sys.exit()
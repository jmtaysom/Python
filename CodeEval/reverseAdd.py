# -*- coding: utf-8 -*-
"""
Created on Fri May 13 09:26:49 2016

@author: jmtaysom
"""
import sys

def is_pal(word):
    word = str(word)
    if word == word[::-1]:
        return True
    else:
        return False

def reverse_add(num,iterations=0):
    #print(num,iterations)
    if is_pal(num):
        print('{} {}'.format(iterations,num))
    else:
        reverse = int(str(num)[::-1])
        reverse_add(num+reverse, iterations=iterations+1)

with open(sys.argv[1],'r') as f:
    for l in f:
        l = l.rstrip()
        l = int(l)
        reverse_add(l)        
        
sys.exit()
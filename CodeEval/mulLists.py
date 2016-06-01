# -*- coding: utf-8 -*-
"""
Created on Fri May 13 09:26:49 2016

@author: jmtaysom
"""
import sys

def mul_lists(l1,l2):
    out = []
    combine = list(zip(l1,l2))
    for pair in combine:
        out.append(pair[0] * pair[1])
    out = [str(x) for x in out]
    return out

with open('sample.txt','r') as f:
    for l in f:
        l = l.rstrip()
        l1,l2 = l.split('|')   
        l1 = l1.split(' ')
        l2 = l2.split(' ')
        l1 = [int(x) for x in l1 if x != '']
        l2 = [int(x) for x in l2 if x != '']
        print(' '.join(mul_lists(l1,l2)))
        
sys.exit()

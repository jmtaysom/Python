# -*- coding: utf-8 -*-
"""
Created on Thu May 19 14:36:37 2016

@author: jmtaysom
"""

alpha = {'1':'1',
         '2':'abc',
         '3':'def',
         '4':'ghi',
         '5':'jkl',
         '6':'mno',
         '7':'pqrs',
         '8':'tuv',
         '9':'wxyz',
         '0':'0'}

def rec_print(string,out=''):
    global final
    for a in alpha[string[0]]:
        if len(string) > 1:
            rec_print(string[1:], out=out+a)
        else:
            final.append(''.join(out+a))

with open('sample.txt', 'r') as f:
    for line in f:
        line = line.rstrip()        
        final = []
        rec_print(line)
        print(','.join(final))
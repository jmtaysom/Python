# -*- coding: utf-8 -*-
"""
Created on Fri May 13 12:37:55 2016

@author: jmtaysom
"""

def recursive_print(n,string,out=''):
    global final
    for letter in string:
        if n>1:
            recursive_print(n-1,string,out=out+letter)
        else:
            final += out+letter+','
           
            

with open('sample.txt', 'r') as f:
    for line in f:
        n, chars = line.split(',')
        n = int(n)
        chars = list(set(chars[:-1]))
        chars.sort()
        final = ''        
        recursive_print(n,chars)
        final = final.split(',')        
        print(*final[:-1], sep=',')
        
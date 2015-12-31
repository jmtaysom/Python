# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 18:57:07 2015

@author: jmtaysom
"""
dividers = range(1,20)

divided = True
  
start = 10  
while divided:
    for i in dividers:
        if start % i != 0:
            start += 10
            break
    else:
        divided = False
        print start

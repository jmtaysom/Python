# -*- coding: utf-8 -*-
"""
Created on Sun Mar 27 10:34:50 2016

@author: jmtaysom
"""

for x in range(1,101):
    if x%3 == 0 and x%5 == 0:
        print('Fizzbuzz', end=', ')
    elif x%3 == 0:
        print('fizz',end=', ')
    elif x%5 == 0:
        print('buzz',end=', ')
    else: 
        print(x,end=', ')
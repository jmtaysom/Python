# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 18:08:10 2015

@author: jmtaysom
"""

a,b = 1,1
even = 0


while b < 4000000:
    a, b = b, a + b
    if b % 2 == 0:
        even += b
        print(b)
print(even)

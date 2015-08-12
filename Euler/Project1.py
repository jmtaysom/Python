# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 21:20:17 2015

@author: jmtaysom
"""
n = 1000
threes = [i for i in range(n) if i%3==0]
fives = [i for i in range(n) if i%5==0]
threefive = set(threes+fives)
print(sum(threefive))


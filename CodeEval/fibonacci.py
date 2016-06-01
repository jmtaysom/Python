# -*- coding: utf-8 -*-
"""
Created on Fri May 13 12:37:55 2016

@author: jmtaysom
"""

def fibo():
    a,b = 0,1
    yield 0
    yield 1
    while True:    
        a,b = b,a+b
        yield b

with open('sample.txt', 'r') as f:
    for line in f:
        fib = fibo()
        for i in range(int(line[:-1])):
            next(fib)
        print(next(fib))
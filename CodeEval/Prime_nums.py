# -*- coding: utf-8 -*-
"""
Created on Fri May 13 09:26:49 2016

@author: jmtaysom
"""
import sys

from math import sqrt


def primes_gen():
    primes = [2,3,5]
    n = 7
    increment = [4,2,4,2,4,6,2,6]
    yield 2
    yield 3
    yield 5
    while True:
        for i in primes[3:int(sqrt(n))]:
            if n % i == 0:
                break
        else:
            primes.append(n)
            yield primes[-1]
        a = increment.pop(0)
        increment.append(a)
        n += a

primes = []
prime_gen = primes_gen()
primes.append(next(prime_gen))

with open('sample.txt','r') as f:
    for l in f:
        l = l.rstrip()
        l = int(l)
        while primes[-1] < l:
            primes.append(next(prime_gen))
        out = [str(p) for p in primes if p < l]
        print(','.join(out))
        
            
        
sys.exit()
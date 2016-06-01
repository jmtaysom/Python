# -*- coding: utf-8 -*-
"""
Created on Fri May 13 09:26:49 2016

@author: jmtaysom
"""

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

def is_pal(word):
    word = str(word)
    if word == word[::-1]:
        return True
    else:
        return False

        
a = primes_gen()
prime = next(a)
prime_pal = 0
while prime < 1000:
    if is_pal(prime):
        prime_pal = prime
    prime = next(a)
print(prime_pal)

sys.exit()

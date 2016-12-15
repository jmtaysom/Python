# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 18:57:07 2015

@author: jmtaysom
"""
from time import time
from collections import Counter
from math import sqrt
t = time()

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


def prime_factors(x,primes):
    pf = Counter()
    while x > 1:
        for prime in primes:
            if x % prime == 0:
                pf[prime] +=1
                x /= prime
    return pf


def smallest_multiple(n):
    primer = primes_gen()
    primes = [next(primer)]
    while max(primes) < n:
        primes.append(next(primer))

    pf = Counter()
    for x in range(2, n+1):

        pf = pf | prime_factors(x,primes)
    total = 1
    for k,v in pf.items():
        total *= k**v
    return total

print(smallest_multiple(20))
print(time() - t)
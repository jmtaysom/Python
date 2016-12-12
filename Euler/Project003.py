# -*- coding: utf-8 -*-
"""
Created on Thurs Dec 17  09:17:35 2015

@author: jmtaysom
"""
from __future__ import division
from math import sqrt


def primes_gen():
    primes = [2,3,5]
    n = 7
    increment = [4,2,4,2,4,6,2,6]
    
    while True:
        yield 2
        yield 3
        yield 5
        for i in primes[3:int(sqrt(n))]:
            if n % i == 0:
                break
        else:
            primes.append(n)
            yield primes[-1]
        a = increment.pop(0)
        increment.append(a)
        n += a


def prime_factors(f):
    primes = primes_gen()
    prime_factors = []

    while f > 1:
        prime = primes.next()
        while f % prime == 0:
            f = f / prime
            prime_factors.append(prime)
    return prime_factors

print prime_factors(600851475143)

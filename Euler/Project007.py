# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 20:42:01 2015

@author: jmtaysom
"""

from math import sqrt
import time



def find_prime(prime):
    Primes = [2,3,5]
    x = len(Primes)
    n = 7
    increment = [4,2,4,2,4,6,2,6]
    
    while x <prime:
        srn =  int(sqrt(n))
        for i in Primes[3:srn]:
            if n % i == 0:
                break
        else:
            Primes.append(n)
            x += 1
        a = increment.pop(0)
        increment.append(a)
        n += a
    print(Primes[-1])

#n = 1000
#t0 = time.time()
#for i in range(n): find_prime(10001)
#t1 = time.time()

#total_n = t1-t0

#print(total_n/n)
print(find_prime(100000))

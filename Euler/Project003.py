# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 18:17:52 2015

@author: jmtaysom
"""
from math import sqrt

def find_prime(prime):
    Primes = [2,3,5]
    x = len(Primes)
    n = 7
    increment = [4,2,4,2,4,6,2,6]
    
    while n <prime:
        srn =  int(sqrt(n))
        for i in Primes[3:srn]:
            if n % i == 0 and prime % n == 0:
                print(n)                
                break
        else:
            Primes.append(n)
            x += 1
        a = increment.pop(0)
        increment.append(a)
        n += a
    return Primes
    
goal = 600851475143    
    
#primes = find_prime(goal/2)
#print('Found the primes')
#primes.sort(reverse=True)
#factors = []
#for prime in range(1,int(goal/2)+1):
#    if goal % prime == 0:
#        factors.append(prime)
#print(prime)
find_prime(goal)
from __future__ import division
from math import sqrt

def primes_gen():
    counter = 0
    primes = [2,3,5]
    n = 7
    increment = [4,2,4,2,4,6,2,6]
    
    while True:
        if counter == 0:
            yield 2
            counter += 1
        elif counter == 1:
            yield 3
            counter += 1
        elif counter == 2:
            yield 5
            counter += 1
        else:
            for i in primes[3:int(sqrt(n))]:
                if n % i == 0:
                    break
            else:
                primes.append(n)
                yield primes[-1]
            a = increment.pop(0)
            increment.append(a)
            n += a
        
def sum_primes(largest):
    primes = primes_gen()
    prime = primes.next()
    prime_list = []
    total = 0
    while prime < largest:
        total += prime
        prime_list.append(prime)
        prime = primes.next()
        
    return total

print sum_primes(2000000)

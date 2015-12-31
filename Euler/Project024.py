from itertools import permutations

a = permutations('0123456789')
for _ in xrange(1000000):
    b = a.next()
c = ''
for i in b:
    c += i

print c

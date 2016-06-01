def pal10(num):
    word = str(num)
    return word == word[::-1]

def pal2(num):
    word = '{0:b}'.format(num)
    return word == word[::-1]

total = 0

for i in xrange(1000000):
    if pal10(i) and pal2(i):
        total += i

print total

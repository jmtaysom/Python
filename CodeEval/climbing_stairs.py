from __future__ import print_function
import sys


a,b = 0,1
fibo = {}
for i in range(1,1001):
    a,b = b,a+b    
    fibo[str(i)] =b 



with open('sample.txt', 'r') as f:
    for line in f:
        line = line.rstrip()
        if line != '':
            print(fibo[line])
            
sys.exit()


#
#def stairs(num):
#    total = 0
#    num = int(num)
#    for i in range((num//2)+1):
#        single_steps = num - i*2
#        total += (factorial(num-i)/(factorial(i)*factorial(single_steps)))
#    return int(total)

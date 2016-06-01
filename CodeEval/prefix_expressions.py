from __future__ import print_function, division
import sys

string = '* + 2 3 4'
def prefix(string):
    sl = string.split(' ')
    half = len(sl)//2
    operators = sl[:half]
    numbers = sl[half:]
    numbers = [int(x) for x in numbers]
    start = numbers.pop(0)
    
    for num in numbers:
        op = operators.pop()
        if op == '*':
            start *= num
        elif op == '/':
            start /= num
        else:
            start += num
    return int(start)


with open(sys.argv[1],'r') as f:
    for l in f:
        l = l.rstrip()
        if l != '':
            print(prefix(l))
            
sys.exit()
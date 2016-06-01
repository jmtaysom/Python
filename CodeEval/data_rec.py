# -*- coding: utf-8 -*-
"""
Created on Fri May 13 09:26:49 2016

@author: jmtaysom
"""
import sys

def recover(line):
    message, order = line.split(';')
    message = message.split(' ')
    order = order.split(' ')
    out =[]
    for i in order:
        out.append(message[int(i)-1])
    while len(message) > 1:
        out.append(message.pop())
    out = ' '.join(out)
    return out

with open('sample.txt','r') as f:
    for l in f:
        l = l.rstrip()
        print(recover(l))
        
        
sys.exit()
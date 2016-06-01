# -*- coding: utf-8 -*-
"""
Created on Thu May 12 20:09:35 2016

@author: jmtaysom
"""
import sys

with open('SampleFB.txt','r') as lines:
    for line in lines:
        if len(line) > 0:            
            fbn = [int(i) for i in line.split()]
            f,b,n = fbn
            result = ''
            for j in range(1,n+1):
                if j % (f*b) == 0:
                    result += 'FB '
                elif j%b == 0:
                    result += 'B '
                elif j%f == 0:
                    result += 'F '
                else:
                    result += str(j)+ ' '
        
            print(result[:-1])
        
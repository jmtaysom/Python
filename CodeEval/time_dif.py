# -*- coding: utf-8 -*-
"""
Created on Fri May 13 09:26:49 2016

@author: jmtaysom
"""
import sys
from datetime import timedelta, date

def time_dif(t1,t0):
    if t1 > t0:
        return t1-t0
    else:
        return t0-t1
 
def time_conv(time):
    time = time.split(':')
    time = [int(t) for t in time]
    time = timedelta(hours=time[0], minutes=time[1], seconds=time[2])
    return time

with open('sample.txt','r') as f:
    for l in f:
        l = l.rstrip()
        t1,t0 = l.split(' ')
        t1 = time_conv(t1)
        t0 = time_conv(t0)
        td = time_dif(t1,t0)
        print('{:0>8}'.format(str(td)))
        
#sys.exit()
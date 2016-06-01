# -*- coding: utf-8 -*-
"""
Created on Fri May 13 09:26:49 2016

@author: jmtaysom
"""
import sys
import re

pattern = '([a-zA-Z0-9]+@[\w]+\.[\w]+)'

with open('sample.txt', 'r') as f:
    for l in f:
        l = l.rstrip()
        if re.match(pattern,l):
            print('true')
        else:
            print('flase')

sys.exit()

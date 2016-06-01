# -*- coding: utf-8 -*-
"""
Created on Fri May 13 12:06:58 2016

@author: jmtaysom
"""

import sys
import re

with open('sample.txt', 'r') as f:
    for line in f:
        sent,sub = line.split(',')        
        result = re.search(sub[:-1], sent)
        if result:
            print('true')
        else:
            print('false')
sys.exit()
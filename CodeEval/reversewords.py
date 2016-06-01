# -*- coding: utf-8 -*-
"""
Created on Fri May 13 09:16:52 2016

@author: jmtaysom
"""

import sys

with open('reversewords.txt', 'r') as f:
    for line in f:
        sample = line.split()
        print(' '.join(sample[::-1]))

sys.exit()
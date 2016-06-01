# -*- coding: utf-8 -*-
"""
Created on Fri May 13 09:26:49 2016

@author: jmtaysom
"""
import sys
import json

def find_labels(string):
    pj = json.loads(string)
    pj_items = pj['menu']['items']
    total = 0    
    for item in pj_items:
        if item is not None:
            if 'label' in item.keys():
                total += item['id']
    return total


with open('sample.txt','r') as f:
    for l in f:
        l = l.rstrip()
        print(find_labels(l))
        
sys.exit()

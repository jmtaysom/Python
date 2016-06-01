# -*- coding: utf-8 -*-
"""
Created on Fri May 13 12:37:55 2016

@author: jmtaysom
"""
from sys import argv
from sys import exit as sysexit

money = [[100.0, 'ONE HUNDRED'],[50.0, 'FIFTY'], [20.0, 'TWENTY'],
         [10.0, 'TEN'], [5.0, 'FIVE'], [2.0, 'TWO'], [1.0, 'ONE'],
         [0.5, 'HALF DOLLAR'], [0.25, 'QUARTER'], [0.1, 'DIME'],
         [0.05, 'NICKEL'], [0.01, 'PENNY']]

def change(value):
    total = []
    while value > 0.01:    
        for amount in money:
            if amount[0] <= value:
                value -= amount[0]
                total.append(amount[1])
                break
    return ','.join(total)


def return_change(owed,payed):
    owed = float(owed)
    payed = float(payed)    
    if payed < owed:
        return 'ERROR'
    elif payed == owed:
        return 'ZERO'
    else:
        return change(payed-owed)
        
            

with open('sample.txt', 'r') as f:
    for l in f:
        if l != '\n':        
            l = l.rstrip()
            #l = set([c.lower() for c in l])
            print(return_change(*l.split(';')))
        
sysexit()
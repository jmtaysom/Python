# -*- coding: utf-8 -*-
"""
Created on Mon May 23 20:47:45 2016

@author: jmtaysom
"""

import sys

def age_checker(age):
    age = int(age)
    if age < 0:
        return "This program is for humans"
    elif age < 3:
        return 'Still in Mama\'s arms' 
    elif age < 5:
        return 'Preschool Maniac' 
    elif age <12:
        return 'Elementary school' 
    elif age < 15:
        return 'Middle school' 
    elif age <19:
        return 'High school' 
    elif age < 23:
        return 'College'
    elif age <66:
        return 'Working for the man' 
    elif age < 101:
        return 'The Golden Years' 
    else:
        return "This program is for humans"
        
with open('sample.txt' ,'r') as f:
    for l in f:
        l = l.rstrip()
        if l != '':
            print(age_checker(l))
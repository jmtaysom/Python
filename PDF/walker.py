# -*- coding: utf-8 -*-
"""
Created on Thu Dec 31 09:20:10 2015

@author: jmtaysom
"""
import os

for root, dirs, files in os.walk(r'/home/jmtaysom/Python/PDF'):
    for file in files:
        if file.endswith(".pdf"):
             print(os.path.join(root, file))
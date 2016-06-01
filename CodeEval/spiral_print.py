# -*- coding: utf-8 -*-
"""
Created on Thu May 19 17:28:04 2016

@author: jmtaysom
"""

def spiral_print(matrix):
    m = len(matrix[0])
    n = len(matrix)
    while m> 0 and n > 0:
        try:
            for i in range(m):
                print(matrix[0].pop(0), end = ' ')
            for j in range(n-2):
                print(matrix[j+1].pop(), end = ' ')
            for k in range(m):
                print(matrix[-1].pop(), end= ' ')
            for l in range(n-2,0,-1):
                print(matrix[l].pop(0), end = ' ')
        except IndexError:
            break
        if m > 2 and n > 2:
            m -= 2
            n -=2
            matrix = [row for row in matrix if len(row) > 0]

def matrixfy(m,n,string):
    m = int(m)
    n = int(n)
    num_list = string.split(' ')
    matrix = []
    for i in range(n):
        row = []
        for j in range(m):
            row.append(num_list.pop(0))
        #row = [int(x) for x in row]
        matrix.append(row)
    return matrix

with open('sample.txt', 'r') as f:
    for line in f:
        if line != '\n':
            l = line.strip()
            m, n, string = l.split(';')
            matrix = matrixfy(m,n,string)
            spiral_print(matrix)
            print()
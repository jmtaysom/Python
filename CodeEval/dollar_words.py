# -*- coding: utf-8 -*-
"""
Created on Fri May 20 07:20:41 2016

@author: jmtaysom
"""

num_dict = {'1': 'One','2': 'Two','3': 'Three','4': 'Four','5': 'Five',
            '6': 'Six','7': 'Seven','8': 'Eight','9': 'Nine'}
teen_dict = {'10': 'Ten','11': 'Eleven','12': 'Twelve','13': 'Thirteen',
             '14': 'Fourteen','15': 'Fifteen','16': 'Sixteen',
             '17': 'Seventeen','18': 'Eighteen','19': 'Nineteen'}
ten_dict = {'2': 'Twenty','3': 'Thirty','4': 'Forty','5': 'Fifty',
            '6': 'Sixty','7': 'Seventy','8': 'Eighty','9': 'Ninety'}
thousands = ['Thousand', 'Million']

num = '1'

def grouping(num):    
    groups = []
    num_len = len(num)
    
    if num_len <= 3:
        groups.append(num)
    elif num_len <= 6:
        groups.append(num[-3:])
        groups.append(num[:-3])
    else:
        groups.append(num[-3:])
        groups.append(num[-6:-3])
        groups.append(num[:-6])
    return groups

def upto_thousand(num):
    num_len = len(num)
    string = ''
    if num[-2:] in teen_dict.keys():
        string += teen_dict[num[-2:]]
    elif num[-1] in num_dict.keys():
        string += num_dict[num[-1]]
        if num_len >1 and num[-2] in ten_dict.keys():
            string = ten_dict[num[-2]] + string
    elif num_len >1 and num[-2] in ten_dict.keys():
        string = ten_dict[num[-2]] + string
    if num_len == 3 and num[-3] in num_dict.keys():
        string = num_dict[num[-3]] + 'Hundred' + string
        
    return string
    

def word_conv(groups):
    groups_len = len(groups)
    if groups_len == 1:
        string = upto_thousand(groups[0])
    elif groups_len == 2:
        string = upto_thousand(groups[1]) + 'Thousand'
        string += upto_thousand(groups[0])
    else:
        string = upto_thousand(groups[2]) + 'Million'
        string += upto_thousand(groups[1]) + 'Thousand'
        string += upto_thousand(groups[0])
    return string

with open('sample.txt', 'r') as f:
    for line in f:
        line = line.rstrip()
        if line != '\n':
            groups = grouping(line)   
            word = word_conv(groups)
            if word == 'One':
                print(word+'Dollar')
            else:
                print(word+'Dollars')
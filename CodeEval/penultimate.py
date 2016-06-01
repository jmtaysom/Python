# -*- coding: utf-8 -*-
"""
Created on Fri May 13 09:26:49 2016

@author: jmtaysom
"""
import sys

morse_dict = {'-': 'T', '--': 'M', '---': 'O', '----.': '9', '---..': '8', 
              '--...': '7', '--.': 'G', '--.-': 'Q', '--..': 'Z', '-....': '6', 
              '-.': 'N', '-.-': 'K', '-.--': 'Y', '-.-.': 'C', '-..': 'D', 
              '-..-': 'X', '-...': 'B', '.....': '5', '.': 'E', '.-': 'A', 
              '.--': 'W', '.---': 'J', '-----': '0', '.--.': 'P', '.-.': 'R', 
              '.-..': 'L', '..': 'I', '..-': 'U', '.----': '1', '..-.': 'F', 
              '...': 'S', '...-': 'V', '..---': '2', '....': 'H', '...--': '3', 
              '....-': '4', ' ': ' '}

def morse_trans(morse):
    out = ''
    for char in morse:
        out += morse_dict[char]
    return out

with open('sample.txt','r') as f:
    for l in f:
        l = l.rstrip()
        l = l.split('  ')
        final = []
        for morse in l:
            morse = morse.split(' ')
            final.append(morse_trans(morse))
        print(' '.join(final))
            
        
sys.exit()

from __future__ import print_function
import sys

def recursive_print(string_list, out=''):
    global output    
    for char in string_list:
        if len(string_list) > 1:
            new_list = [c for c in string_list if c != char]
            recursive_print(new_list,out=(out+char))
        else:
            output.append(out+char)

with open(sys.argv[1] ,'r') as f:
    for l in f:
        l = l.rstrip()
        if l != '':
            sl = [ c for c in l]
            sl.sort()
            output = []           
            recursive_print(sl)
            print(','.join(output))
            
sys.exit()
from __future__ import print_function
import sys

num_dict = {'eight': 8, 'five': 5, 'four': 4, 'nine': 9,
            'one': 1, 'seven': 7, 'six': 6, 'three': 3, 'two': 2}
teen_dict = {'eighteen': 18, 'eleven': 11, 'fifteen': 15,
             'fourteen': 14, 'nineteen': 19, 'seventeen': 17,
             'sixteen': 16, 'ten': 10, 'thirteen': 13, 'twelve': 12}
ten_dict = {'eighty': 8, 'fifty': 5, 'forty': 4, 'ninety': 9,
            'seventy': 7, 'sixty': 6, 'thirty': 3, 'twenty': 2}
    
def text2hun(string):
    number = 0
    if 'hundred' in string:
        hun,tens = split_text(string)
        number += (num_dict[hun] * 100)
        string = tens
    if ' ' in string:
        tens, ones = string.split(' ')
        number += (ten_dict[tens] * 10)
        number += num_dict[ones]
    elif string in teen_dict:
        number += teen_dict[string]
    elif string in ten_dict:
        number += (ten_dict[string] * 10)
    elif string in num_dict:
        number += num_dict[string]
    return number
   
def text2word(string):
    number = 0
    neg = 'negative' in string
    if neg:
        string = string[9:]
    if 'million' in string:
        mil, string = split_text(string, by='million')
        number += (text2hun(mil) * 1000000)
    if 'thousand' in string:
        thou, string = split_text(string, by='thousand')
        number += (text2hun(thou) * 1000)
    if len(string) > 0:
        number += text2hun(string)
    if neg:
        number *= -1
    return number


def split_text(string, by='hundred'):
    out = string.split(by)
#    if 'hundred' in out[0]:
#        out[0] = out[0][:-7]
    out = [s.strip() for s in out]
    if len(out) == 1:
        out.append('')
    #print(out,by)
    return (out[0], out[1])

with open('sample.txt', 'r') as f:
    for line in f:
        line = line.rstrip()
        line = line.strip('\'')
        if line != '\n':
            print(text2word(line))
            
#sys.exit()
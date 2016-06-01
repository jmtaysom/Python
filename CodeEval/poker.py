
from __future__ import print_function
import sys
from collections import Counter

card_vals = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8,
             '9':9, 'T':10, 'J':11, 'Q':12, 'K':13, 'A':14}

hand1 = '6D 7H AH 7S QC'

def read_hand(string):
    cards = string.split(' ')
    values = [card[0] for card in cards]
    suites = [card[1] for card in cards]
    flush = len(set(suites)) == 1
    num_vals = [card_vals[val] for val in values]
    num_vals.sort()
    high_card = num_vals[4]
    straight = (high_card-num_vals[0]) == 4
    pairs = Counter(values)
    cards_mc = pairs.most_common()
    if flush and straight and high_card == 14:
        hand_value = 10
        best = 14
    elif flush and straight:
        hand_value = 9
        best = high_card
    elif cards_mc[0][1] == 4:
        hand_value = 8
        best = int(card_vals[cards_mc[0][0]])
    elif cards_mc[0][1] == 3 and cards_mc[1][1] == 2:
        hand_value = 7
        best = int(card_vals[cards_mc[0][0]])
    elif flush:
        hand_value = 6
        best = high_card
    elif straight:
        hand_value = 5
        best = high_card
    elif cards_mc[0][1] == 3:
        hand_value = 4
        best = int(card_vals[cards_mc[0][0]])
    elif cards_mc[0][1] == 2 and cards_mc[1][1] == 2:
        hand_value = 3
        best = int(card_vals[cards_mc[0][0]])
    elif cards_mc[0][1] == 2:
        hand_value = 2
        best = int(card_vals[cards_mc[0][0]])
    else:
        hand_value = 1
        best = high_card
    
    return (hand_value,num_vals,best)

def tie_breaker(h1,b1,h2,b2):
    if b1 >b2:
        return 'right'
    elif b2 > b1:
        return 'left'
    else:
        for i in range(5):
            dif = h1[i] - h2[i]
            if dif == 0:
                pass
            elif dif > 0:
                return 'left'
            else:
                return 'right'
        
def winner(h1,h2):
    h1 = read_hand(h1)
    h2 = read_hand(h2)
    dif = h1[0] - h2[0]
    if dif == 0:
        tie_breaker(h1[1],h1[2], h2[1], h2[2])
    elif dif > 0:
        return 'left'
    else:
        return 'right'

with open('sample.txt' ,'r') as f:
    for l in f:
        l = l.rstrip()
        if l != '':
            h1 = l[:14]
            h2 = l[15:]
            print(winner(h1,h2))
            
sys.exit()
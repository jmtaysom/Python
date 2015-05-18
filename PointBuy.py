# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import random
import statistics
import matplotlib.pyplot as plt
import os
from math import floor

random.seed(0)

d6 = [1,2,3,4,5,6]
points = {3:-5, 4:-4, 5:-3, 6:-2, 7:-1, 8:0, 9:1, 10:2, 11:3, 12:4, 13:5, 14:6, 
          15:8, 16:10, 17:13, 18:16}

def roll_atr():
    ''' Roll four dice and drop the lowest'''    
    atr = []
    for i in range(4):
        atr.append(random.choice(d6))
    atr.sort()
    atr.pop(0)
    return sum(atr)

def calc_bonus(stat):
    '''take a stat and calculate its bonus value'''    
    return floor((stat - 10)/2)

def roll_stats():
    '''Roll 6 stats, check for the need to reroll'''    
    # Roll 6 stats   
    stats = []    
    for i in range(6):
        stats.append(roll_atr())
    # Check to make sure there is at least one stat over 13 and that the sum of
    # the bonuses is positive. If not re-roll
    while max(stats) <=13 or sum(map(calc_bonus,stats))<=0:
        stats = []    
        for i in range(6):
            stats.append(roll_atr())    
    return stats
    
def point_calc(stats):
    # Convert the stats into their point values and return the sum of the points
    output_list = []
    for stat in stats:
        point = points.get(stat)
        output_list.append(point)
    total = sum(output_list)
    return(total)
    

if __name__ == '__main__':
    all_rolls = []    
    for i in range(100000):
        a = point_calc(roll_stats())
        #if a:
        all_rolls.append(a)
    print('Mean: ',statistics.mean(all_rolls), 'SD: ',
          statistics.stdev(all_rolls), 'Median: ',
          statistics.median(all_rolls), 'Mode: ', statistics.mode(all_rolls))
    #plt.hist(all_rolls) 
    #plt.show()
    #plt.savefig('point_buy5.png')
    #os.system('eog point_buy5.png &')
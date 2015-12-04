# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 12:43:03 2015

@author: jmtaysom
"""
import numpy as np




def checkio(game_result):
    test_array = np.array([list(x) for x in game_result])
    if any([all(x == 'X') for x in test_array]):
        return('X')
    elif any([all(x == 'X') for x in test_array.transpose()]):
        return('X')
    elif any([all(x == 'O') for x in test_array]):
        return('O')
    elif any([all(x == 'O') for x in test_array.transpose()]):
        return('O')
    elif all(test_array.diagonal() == 'X') or all(np.fliplr(test_array).diagonal() == 'X'):
        return('X')
    elif all(test_array.diagonal() == 'O') or all(np.fliplr(test_array).diagonal()  == 'O'):
        return('O')
    else:
        return('D')
        


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        "X.O",
        "XX.",
        "XOO"]) == "X", "Xs wins"
    assert checkio([
        "OO.",
        "XOX",
        "XOX"]) == "O", "Os wins"
    assert checkio([
        "OOX",
        "XXO",
        "OXX"]) == "D", "Draw"
    assert checkio([
        "O.X",
        "XX.",
        "XOO"]) == "X", "Xs wins again"


        
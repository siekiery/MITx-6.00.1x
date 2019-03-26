# -*- coding: utf-8 -*-
"""
Created on Sat Nov 24 13:26:59 2018

@author: Jakub Pitera
"""

def how_many(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    sum = 0
    for v in aDict.values():
        sum += len(v)
    return sum

animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

print(how_many(animals))
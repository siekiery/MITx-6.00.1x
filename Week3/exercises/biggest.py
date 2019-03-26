# -*- coding: utf-8 -*-
"""
Created on Sat Nov 24 13:26:59 2018

@author: Jakub Pitera
"""

def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    aDict_len= {}
    for key in aDict:
        aDict_len[key]=len(aDict[key])
        
    return max(aDict_len, key = lambda k: aDict_len[k])

animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

print(biggest(animals))
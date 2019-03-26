# -*- coding: utf-8 -*-
"""
Created on Fri Nov 23 17:29:09 2018

@author: Jakub Pitera
"""



def applyToEach(L, f):
    for i in range(len(L)):
        L[i] = f(L[i])

def multbyfive(x):
    return x * 5

def add_one(x):
    return x +1

def square(x):
    return x*x

testList = [1, -4, 8, -9]

applyToEach(testList, abs)

print(testList)
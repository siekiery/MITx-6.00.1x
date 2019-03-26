# -*- coding: utf-8 -*-
"""
Created on Sun Nov 18 12:29:40 2018

@author: Jakub Pitera
"""

"""
Problem 2

Assume s is a string of lower case characters.
Write a program that prints the number of times the string 'bob' occurs in s. 
For example, if s = 'azcbobobegghakl', then your program should print
"Number of times bob occurs is: 2"
"""

s = input("Input: ")

bobcount = 0

for c in range(2,len(s)):
    first = s[c-2]
    second = s[c-1]
    third = s[c]
    if first+second+third == 'bob':
            bobcount += 1
            
print("Number of times bob occurs is: ",bobcount)
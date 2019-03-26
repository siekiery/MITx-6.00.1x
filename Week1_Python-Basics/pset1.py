# -*- coding: utf-8 -*-
"""
Created on Sun Nov 18 12:29:41 2018

@author: Jakub Pitera
"""

"""
Problem 1

Assume s is a string of lower case characters.
Write a program that counts up the number of vowels contained in the string s. 
Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. For example,
if s = 'azcbobobegghakl', your program should print: "Number of vowels: 5"
"""

s=input("Input: ")
vowels = ['a','e','i','o','u']
CountVow=0
for char in s:
    if char in vowels:
        CountVow +=1 
print("Number of vowels: ",CountVow)
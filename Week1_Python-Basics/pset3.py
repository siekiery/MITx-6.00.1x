# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 21:05:37 2018

@author: Jakub Pitera
"""

"""
Problem 3

Assume s is a string of lower case characters.
Write a program that prints the longest substring of s in which the letters 
occur in alphabetical order. For example, if s = 'azcbobobegghakl', then your
program should print: Longest substring in alphabetical order is: beggh"

In the case of ties, print the first substring. For example, if s = 'abcbcd', 
then your program should print 
"Longest substring in alphabetical order is: abc"
"""

# Input
s = input("Input: ")

# Declarations
abc_word = ''
abc_word_longest = ''
abc_list = []

# Iterates over every char in a string
for c in range(len(s)):
    
    #Initiates first word
    if abc_word == '':
        abc_word = s[c] 
        
    # Stores current char in a word if it's in order
    elif s[c] >= s[c-1]:
        abc_word += s[c]
        # In case this is the last char it proceeds to add word to the list
        if c == len(s)-1:
            if len(abc_word) > len(abc_word_longest):
                abc_word_longest = abc_word
            abc_list += [abc_word]
            
    # If current char is not ordered it checks to save longest word and stores
    # currently  conjured word in a list and begins conjuring new one
    else:
        if len(abc_word) > len(abc_word_longest):
            abc_word_longest = abc_word
        abc_list += [abc_word]
        abc_word = s[c]
 
print("Longest substring in alphabetical order is: ",abc_word_longest)
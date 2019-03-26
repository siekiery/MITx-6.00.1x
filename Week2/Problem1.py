# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 21:05:58 2018

@author: Jakub Pitera
"""
'''
Problem 1 - Paying Debt off in a Year

Write a program to calculate the credit card balance after one year if a
person only pays the minimum monthly payment required by the credit card
company each month.

The following variables contain values as described below:
balance - the outstanding balance on the credit card
annualInterestRate - annual interest rate as a decimal
monthlyPaymentRate - minimum monthly payment rate as a decimal

For each month, calculate statements on the monthly payment and 
remaining balance. At the end of 12 months, print out the remaining 
balance. 

A summary of the required math is found below:
Monthly interest rate= (Annual interest rate) / 12.0
Minimum monthly payment = (Minimum monthly payment rate) 
        x (Previous balance)
Monthly unpaid balance = (Previous balance) - (Minimum monthly payment)
Updated balance each month = (Monthly unpaid balance)
        + (Monthly interest rate x Monthly unpaid balance)
'''


def UpdatedBalanceEachMonth(balance,annualInterestRate,monthlyPaymentRate):
    MIR = annualInterestRate / 12.0     #Monthly Interest Rate
    MMP = monthlyPaymentRate*balance    #Minimum Monthly Payment
    MUB = balance-MMP                   #Monthly Unpaid Balance
    return MUB+MIR*MUB

    
def UpdatedBalanceAfterYear(balance,annualInterestRate,monthlyPaymentRate):
    for i in range(12):
        balance = UpdatedBalanceEachMonth(
                balance,annualInterestRate,monthlyPaymentRate)
    print("Remaining balance: ",round(balance,2))

balance = 42
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

UpdatedBalanceAfterYear(balance,annualInterestRate,monthlyPaymentRate)
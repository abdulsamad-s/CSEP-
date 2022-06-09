# -*- coding: utf-8 -*-
"""
Created on Thu Jun  9 09:48:59 2022

@author: Samad
"""
def factorial(number):
    if number <0:
        return 'Factorial does not exist as it is Negative '
    elif number==0 or number==1:
        return 1 #Because 0!=1 & 1!=1
    else:
        return number*factorial(number-1) #n!=n*(n-1)*(n-2)*(n-3)*.....*1

#lets check some examples
print(factorial(0))
print(factorial(-6))
print(factorial(4))



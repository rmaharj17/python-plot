# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 11:20:30 2019

@author: ChemGrad
"""

"""
# We have to find answers
y = [1, 3, 5, 7, 9]
total = 0

for i in y:
    total += i
    if i > 5:
        break
print(total)

x = 5
while x < 10:
    x += 2
print(x)

import sys
print(sys.path)
"""

def gcd(a,b):
    while b:
        a, b = b, a%b
    return a

if __name__ == "__main__":

    if gcd(40, 12) == 4:
        print("Everything is okay")
    else:
        print("The GCD function is wrong")
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 13:55:49 2019

@author: ChemGrad
"""

add = lambda x, y: x + y
print(add(4,5))

def add(x, y):
    return x+y
print("\n",add(4,5))

a=[1,2,3]
b=[4,5,6]
c=["bat", "sparrow", "peageon"]

col_format = "{:<5}" * 3 + "\n"   # 3 left-justfied columns with 5 character width

with open("python_file.txt", 'w') as of:
    for x in zip(a, b, c):
        of.write(col_format.format(*x))
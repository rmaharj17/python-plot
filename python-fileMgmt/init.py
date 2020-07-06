# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 09:46:17 2019

@author: ChemGrad
"""

"""
class computer:
    
    def __init__ (self, cpu, ram):
        self.cpu = cpu
        self.ram = ram
        
    def config(self):
        print("Config is:", self.cpu, self.ram)
        
com1 = computer('i5', 16)
com2 = computer('Ryzen-3', 8)

com1.config()
com2.config()
"""


import pandas as pd

data = [["Rajendra", 10], ["Urmila", 7], ["BasaMaya", 8]]
df = pd.DataFrame(data, columns = ["Name", "Jersey"], dtype = int)
f = open("sample.txt", "w+")
table = str(df)
f.write(table)
f.close()
print(table)
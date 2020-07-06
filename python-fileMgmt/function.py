# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 10:13:42 2019

@author: ChemGrad
"""


"""
# Scope and lifetime of variable

def scopeFunc():
    x = 10
    print("The value inside function: ", x)
    return x

x = 20

scopeFunc()
print("The value outside function: ", x)


def prime(n):
    if n < 2:
        return False
    
    i = 2
    while i**2 <= n:
        if n % i == 0:
            return False
        i += 1
    return True

n = int(input("Give an integer to test prime number: "))
print(prime(n))

def reverse(str):
    s = ""
    
    for ch in str:
        output = str + s
        
    return output

str1 = "ILoveusingComputer"
print ("Given string is: ", str1)
print("The reverse string is: ", reverse(str1))
"""


"""
myFile = open("small_hexagonal_ice.txt", "rt")
content = myFile.read()
myFile.close()
print(content)
"""


"""
mylines = []
with open("sample.txt", "rt") as myfile:
    for myline in myfile:
        
        #print(myline)
        
        #print(myline[0:10])
        
        mylines.append(myline)
#print(mylines)
#print(mylines[10])
        
    for element in mylines:
        #print)element)
        #print(element, end = ' ')
        print(mylines[4].find("H2"))
        print(mylines[5].find("H2"))  # -1 if does not locate substring
"""

myfile = open("create_file.txt", "w+")
myfile.write("The apple is red and the berry is blue!")
myfile.close()

myfile = open("create_file.txt", "rt")
line = myfile.read()
myfile.close()
print(line)
print(line.find("is"))
print(line.rfind("is"))
print(line.count("is"))
print(line.startswith("The"))
print(line.endswith("The"))
print(line.replace("apple", "car").replace("berry", "truck"))



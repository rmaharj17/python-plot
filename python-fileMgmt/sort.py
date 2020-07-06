# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 18:55:26 2019

@author: ChemGrad
"""

vowels = ['a', 'u', 'o', 'e', 'i']
vowels.sort()
print("The sorted list is ", vowels)

vowels.sort(reverse = True)
print("The reverse list is ", vowels)

numbers = [5, 3, 7, 4, 9, 2, 3, 8]
numbers.sort()
print("The sorted numbers is ", numbers)

# insertion sort -- easy way to sort

def insertionSort (list):
    for index in range(1, len(list)):
        currentValue = list[index]
        position = index - 1
        
        while position >= 0 and list[position] > currentValue:
            list[position + 1]= list[position]
            position -= 1
        list[position + 1] = currentValue
        
list = []
num = int(input("How many integers do you want to sort?"))
for i in range(num):
    list[i] = input("The number")
insertionSort(list)
print(list)            
        
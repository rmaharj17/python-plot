# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 17:45:38 2019

@author: ChemGrad
"""

def main():
    
    # to get specific lines
    totalLines = 0
    with open("small_hexagonal_ice.txt", "r") as f:
        for line in f:
            totalLines += 1
        print("Number of lines: ", totalLines)
        f.close()
    '''
    f = open("small_hexagonal_ice.txt", 'r')
    f1 = open("O_atoms.txt", 'w+')
    lineNum = 2
    lines = f.readlines()
    while lineNum < (totalLines-1):
        print(lines[lineNum])
        f1.write(lines[lineNum])
        lineNum += 3
    f.close()
    f1.close()
    '''
    
    
    f = open("small_hexagonal_ice.txt", 'r')
    f1 = open("x_axis.txt", 'w+')
    lines = f.readlines()
    result = []
    for x in lines:
        result.append(x.split())
    f.close()
    print(result[3][4])
    
    f = open("small_hexagonal_ice.txt", 'r')
    for i in range(totalLines-1):
        if i > 1:
            f1.write("\n" + "         ")
            f1.write(result[i][3] + "\t" + result[i][4] + "     ")
            # or f1.write(result[i][4] + "     ")
            f1.write(result[i][5] + "\n")
    f1.close()
    f.close()
    
if __name__ == "__main__":
    main()
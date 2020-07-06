# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 09:09:11 2019

@author: ChemGrad
"""
def main():

# open the file back and read the contents
    
    # file_read = open("small_hexagonal_ice.txt", "r")
    
    '''
    # Python Program to Copy the Contents of One File into Another
    with open("small_hexagonal_ice.txt") as f:
        with open("out.txt", "w") as f1:
            for line in f:
                f1.write(line)
    '''
    
    '''
    # Python Program to read the contents of a file
    if file_read.mode == "r":
        # use the read() function to the contents
        contents = file_read.read()
        print(contents)
    '''
    
    f = open("small_hexagonal_ice.txt")
    lines = f.readlines()
    i = 0
    search = 'H1'
    
    while i < 386:
        if lines[i] == search:
            print(lines[i])
            i += 1
    else:
        i += 1
    f.close()
    
if __name__ == "__main__":
    main()
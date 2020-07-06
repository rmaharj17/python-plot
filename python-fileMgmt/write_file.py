# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 11:18:56 2019

@author: ChemGrad
"""

def main():
    # open a file for writing and create it if id does not exist
    f = open("python_file.txt", "w+")
    
    # write some lines of data to teh file
    for i in range(10):
        f.write("This is line %d\r\n" %(i + 1))
    
    # close the file when done
    f.close()
    
    # open a file for writing and create it if id does not exist
    f = open("python_file.txt", "a+")
    
    f.write("\nThis is appended line onward\n")
    # writ some lines of data to the file
    for i in range(5):
        f.write("This is line %d\r\n" %(i+11))
        
    # close the file when done
    f.close()
    
    # open the file back and read the contents
    f = open("python_file.txt", "r")
    
    '''if f.mode == "r":
        # use the read() function to the contents
        contents = f.read()
        print(contents)'''
    
    # or, readlines reads the individual lines
    f1 = f.readlines()
    for x in f1:
        print(x)

# declare a call function for "def main()"
# '==' used for comparison while '=' sign for assignment
if __name__ == "__main__":
    main()
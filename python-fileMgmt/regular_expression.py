# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 12:29:22 2019

@author: ChemGrad
"""

import re

text = "Education is fun, I want to be progressive"
r1 = re.findall(r"^\w+", text)
print(r1)
print(re.split(r'\s', 'we are splitting the words'))
print(re.split(r's', 'split the words'))


import os.path
from os import path
import shutil  # for copy

def main():
    print("\nfile exists:" +str(path.exists("write_file.py")))
    print("file exist:" +str(path.exists("python_file.txt")))
    print("file exists:" +str(path.exists("write.txt")))
    print("directory exists:" +str(path.exists("test_folder")))
    
    
    print("\nIs it File?" +str(path.isfile("write_file.py")))
    print("Is it File?" +str(path.isfile("test_folder")))
    
    print("\nIs it Directory?" + str(path.isdir("write_file.py")))
    print("Is it Directory?" + str(path.isdir("test_folder")))
    
    # copy and rename
    if path.exists("python_file.txt"):
        # get the path to the file in the current directory
        src = path.realpath("python_file.txt");
        print("\n",src)
        
        # separate the path from the filter
        head, tail = path.split(src)
        print("path:" +head)
        print("file:" +tail)
        
        # let's make a backup copy by appending "bak" to the file
        dst = src+".bak"
        
        # now use the shell to make a copy of the file
        shutil.copy(src, dst)
        
        #copy over the permissions, modifications
        shutil.copystat(src, dst)
        
        '''
        # remove the file
        os.remove("python_file.txt.bak")'''
        
        '''# rename the original file
        os.rename("python_file.txt", "copy_python_file.txt")'''
    
if __name__ == "__main__":
    main()
# -*- coding: utf-8 -*-
"""
Created on Sat May 25 11:22:13 2024

@author: admin
"""

# Write a function in python to count the number of lines from a text file "story.txt" which is
# not starting with an alphabet "T".
# Example: If the file "story.txt" contains the following lines:
# A boy is playing there.
# There is a playground.
# An aeroplane is in the sky.
# The sky is pink.
# Alphabets and numbers are allowed in the password.

# The function should display the output as 3

# ----------------------------

# Here we create write mode for write data in story.txt file 
# we use with open because we not need to close file manually 
# At first parameter we have to give proper location in which file is stored
# after extracting zip file path may be mismatch

with open("story.txt",'w+') as f1:
    f1.writelines("A boy is playing there. \n")
    f1.write("There is a playground.\n")
    f1.write("An aeroplane is in the sky..\n")
    f1.write("The sky is pink.\n")
    f1.write("Alphabets and numbers are allowed in the password.")


# here we use read mode for read data from file 
    
with open("story.txt","r") as f2:
    count = 0
    
    #  here we use read readline for extracting all data at one time 
    
    data = f2.readlines()
    # we use this for checking data type, of elements in data which is in list format
    # for i in data:
    #     print(type(i))
        
    for i in data :
        if i[0] != 'T':
            count += 1
    print("Count of Lines Start from Alphabet T : " , count)



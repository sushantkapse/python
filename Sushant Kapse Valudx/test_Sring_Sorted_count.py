# -*- coding: utf-8 -*-
"""
Created on Sat May 25 10:35:00 2024

@author: admin
"""


# Write a program to compute the frequency of the words from the input. The output should
# output after sorting the key alphanumerically. Suppose the following input is supplied to the
# program:
    
#------------------------------------ 
 
# Take input in string format     
str1 = input("Enter Input : ")

#  use dictionary for storing the output 
#  dictionary because keys never be repeated
dict1 = {}

# split string for iterating string values for counting the count
l1 = str1.split(" ")

# iterate the list add count in dictionary

for i in l1:
    count = 1
    if i  in dict1:
        count+= 1
    dict1[i] = count
        
print(dict1)


# sort the keys because using sorted function and print it.
for i in sorted(dict1.keys()):
        print(f"{i} : {dict1[i]}")










   
    

   



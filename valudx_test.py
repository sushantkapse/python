# -*- coding: utf-8 -*-
"""
Created on Sat May 25 10:35:00 2024

@author: admin
"""


# Write a program to compute the frequency of the words from the input. The output should
# output after sorting the key alphanumerically. Suppose the following input is supplied to the
# program:
    
    
# str1 = input("Enter Input : ")
# dict1 = {}
# l1 = str1.split(" ")

# for i in l1:
#     count = 1
#     if i  in dict1:
#         count+= 1
#     dict1[i] = count
        
# print(dict1)



# for i in sorted(dict1.keys()):
#         print(f"{i}:{dict1[i]}")


# with open("story.txt",'w+') as f1:
#     f1.writelines("A boy is playing there. \n")
#     f1.write("There is a playground.\n")
#     f1.write("An aeroplane is in the sky..\n")
#     f1.write("The sky is pink.\n")
#     f1.write("Alphabets and numbers are allowed in the password.")

    
# with open("story.txt","r") as f2:
#     count = 0
#     data = f2.readlines()
#     # for i in data:
#     #     print(type(i))
        
#     for i in data :
#         if i[0] != 'T':
#             count += 1
#     print(count)




import math

class myerror(Exception):
    pass
try:
    a =input("Enter String : ")
    if a.isdigit():
    
        raise myerror

   
        
    if a == a[::-1]:
        
        print("This string is Pallindrome ")
    else :
        print("String is not pallindrome ")
            
except myerror :
    print("Enter a Valid String ")
    

   
    

   



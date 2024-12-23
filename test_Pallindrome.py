# -*- coding: utf-8 -*-
"""
Created on Sat May 25 11:28:16 2024

@author: admin
"""

# A palindrome is a string that reads the same backward as forward. For example, the words dad,
# madam and radar are all palindromes. Write a programs that determines whether the string is a palindrome.

# Note: do not use reverse() method

# ---------------------------------------------

#  Inherit Exception class for creating customized exception
# class myerror(Exception):
#     pass

# #  exception try block
# try:
#     a =input("Enter String : ")
    
#     # here we check is there digit is present or not then it will raise error
#     for i in a:
#         if i.isdigit():
#             raise myerror
   
    
       

   
#     # check string is reverse or not by using string method 
#     if a == a[::-1]:
        
#         print("This string is Pallindrome ")
#     else :
#         print("String is not pallindrome ")
        

# #  here write method is shown when myerror exception is raised            
# except myerror :
#     print("Enter a Valid String ")













# str1 = input("Enter str : ")
# n = len(str1)
# flag = True
# for i in range(len(str1)//2):
#     if str1[i] != str1[n-1-i]:
#         flag = False
# if flag:
#     print("true")

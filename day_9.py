# -*- coding: utf-8 -*-
"""
Created on Sat Apr 27 10:07:53 2024

@author: admin
"""

# recurssion
# program counter 
# satck register

# base case 
# process
# sum = 0
# while True:
#     n = int(input("enter no : "))
#     if n <= 0:
#         break
#     else:
#        sum+= n
# print(sum)


# def add(n):
#     if n <= 0:
#         return 0
#     else:
#         n = int(input("enter no : "))
#         return n + add(n)
# a = add(8)

# def power(a,b):
    
#     if b == 0:
#         return 1
#     else:
#         b-= 1
#         return a * power(a, b)
    
    
# p = power(3, 4)
# print(p)

# pass = only declaration
# zero 
# value
# name 
# file

# exception handling
# try except
# finally


# line by line error and except block executed linet first error in 
# mhanje pahilyanda pahila except block run honar according to try chya w.rto


# user defined  = raise error 
# we need to define class by this name1
# and we raised to this class by name 


class myerror(Exception):
    pass
try:
    a =int(input("Enter number : "))
    if a < 10:
        raise myerror

    else :
        print(a/0)
except myerror :
    print("Number shoud be greater than zero")
    
except ZeroDivisionError as e:
    print(e)

   



# performance1 = None     
# performance2 = None     
# performance3 = None     
# performance4 = None

# total = 0


# for i in range(4):
    
# class performanceerror(Exception):
#     pass

# i = 1
# while True:
    
#     try:
    
        
#         ticket = int(input(f"Enter ticket for performance {i} : "))
#         if ticket > 0 and ticket <= 120:
            
#             print(f"tickets for performance {i } : " , ticket)
#             i += 1
#             total += ticket
#             if i > 4:
#                 break
#         else:
#             raise performanceerror
        
#     except performanceerror :
#         print("Ticket should be 0 to 120")
       
        
# print("Total Ticket : ", total)   
    
# ------------------------------------------------------------
# # regerx
# ^ = for start with1aAZ
# $ = end
# /s1 = space
# [a-z]+
# [a-z]*
# [a-z]?


import re
# pcode = input("Enter the pcode ")
# pattern = "^[A-Zz]{2}[0-9]{3,6}$"
# check = re.match(pattern, pcode)

# # in this check match object is stored
# if check:
#     print("valid")
# else:
#     print("invalid")

# no = input("enter the number : ")
# pattern = "[A-Z]{2}[\s][0-9]{2}[\s][A-Z]{2}[\s][0-9]{4}$"
# check = re.match(pattern, no)
# if check:
#     print("valid")
# else:
#     print("invalid")
# [-]*[@][gmail,yahoo][.][com,co]

# pattern = "^[a-z]+[0-9]+[-]*[@](gmail|yahoo)[.](com|co)$"
# email = input("Enter email :")
# check = re.match(pattern, email)
# if check:
#     print("valid")
# else:
#     print("invalid")

# search() = return match object
#split()
#findall()

# comment = "product is very good i like it most and it is very good"
# pattern = "(good|most)"
# pattern = "bad"
# pattern = "\s"


comment = "12423friur238ey912e23bry  32ttfufu"
pattern = "[\d]"

v = re.split(pattern, comment)
print(v)
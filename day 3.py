# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 10:16:15 2024

@author: admin
"""

# pattern programmin

# from datetime import date
# cdate = date.today()
# print(cdate)

# year = cdate.year
# month = cdate.month
# date1 = cdate.day

# print("The Date is : ", date1,"/",month,"/",year)

# # issued_date = input("Enter date : ")
# # list1 = issued_date.split("/")
# # if list1[2] 




# pattern programming


# k = 1
# for i in range(0,4):
#     for j in range(0, i+1):
#         print(k,end=" ")
#         k += 1
#     print()

    
    
# a = 0
# for i in range(0,4):
#     n= 3
#     for j in range(0, i+1):
#         print(i+1, end=" ")
#         i = i+n
#         n-= 1
#     print()
# n=4        
# for i in range(0, n):
#     for j in range(0, n):
#         if i == 0 or i == n-1 or j == 0 or j== n-1:
#             print(" 1 ", end=" ")
#         else:
#             print(" ", end=" ")
            
# n = 4
# for i in range(0, n):
#     for j in range(0, n):
#         if i == 0 or i == n-1 or j == 0 or j == n-1:
#             print(" 1 ", end=" ")
#         else:
#             print("   ", end=" ")
#     print()

# Login_id = input("enter login id : ")        
# password = input("enter password : ")   

# store_id = "abc"
# store_password = "abc@123"
# q = False

# while q == False:
#     Login_id = input("enter login id : ")        
#     password = input("enter password : ") 
#     if Login_id == store_id and password == store_password:
#         print("lofin successful")
#         q = True
#     elif Login_id == store_id and password != store_password :
        
#         print("password is wrong")
#     elif Login_id != store_id and password == store_password :
#         print("Login is not valid")
#     else:
#         print("invalid data")


# --------------------
# list1

# li = []
# li = ['@',"34",'$']

# for i in range(3,6):
#     a = input("enter value :")
#     li.append(a)
# print(li)





# import random
# length = random.randint(7, 10)

# password = ""
# for i in range(length):
#     pos = random.randint(33, 126)
#     password += chr(pos)
# print("password :", password)
# print("Password Length : ", len(password))


# import Math




stored_password = "EHQAB6"
check_password=""
count = 2
for i in range(3):
    
    password1 = input("Enter the password :")
    for i in range(0,len(password1)):
        # if(password1[i] != )
        char = ord(password1[i].upper()) + 3
        if char >= 48 and char <= 90  :
            check_password += chr(char)
        else:
            char = char - 26
            check_password += chr(char)
        
    # print(check_password)
    if check_password == stored_password:
        print("correct password ")
        break
    else:
        print("Icorrect Password")
        print("Now You only have ",count ,  "attempts")
    count = count - 1
    # print(count)
    check_password=""
    
   
    


    

    
    
    



    
    
    


    
    
        
        
        
         
    

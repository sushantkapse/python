# -*- coding: utf-8 -*-
"""
Created on Sat Apr 20 12:42:29 2024

@author: admin
# """

# import random
# def generate_licen(old_number_plate,new_number_plate):
    
#     print("All Old Number Plates")
#     for i in range(old_number_plate):
#         str1 = ""
#         for i in range(3):
#             case = random.randint(1, 2)
#             match case :
#                 case 1:
#                     pos = random.randint(65, 90)
#                     str1 += chr(pos)
               
                    
#                 case 2:
#                     pos = random.randint(97, 122)
#                     str1 += chr(pos)
               
       
        
#         for i in range(3):
#             a = random.randint(1, 9)
#             str1 += str(a)
#         print(str1)
        
#     print("All New Number Plates")
#     for i in range(new_number_plate):
#         str1 = ""
#         for i in range(3):
#             case = random.randint(1, 2)
#             match case :
#                 case 1:
#                     pos = random.randint(65, 90)
#                     str1 += chr(pos)
               
                    
#                 case 2:
#                     pos = random.randint(97, 122)
#                     str1 += chr(pos)
               
       
        
#         for i in range(4):
#             a = random.randint(1, 9)
#             str1 += str(a)
#         print(str1)
        
    
# old_number_plate = int(input("Enter How Many Old Number plate in list : "))
# new_number_plate = int(input("Enter How Many New Number plate in list : "))

   
# generate_licen(old_number_plate,new_number_plate)



# name = input("Enter Name : ")
# hourly_pay_rate  = int(input("Your Hourly Pay Rate : "))

# for i in range()

def valid_triangle(s1,s2,s3):
    if s1>=s2+s3 or s2>=s1+s3 or s3>=s1+s2:
        return False
    else:
        return True

s1=int(input("Enter 1st Side length:"))
s2=int(input("Enter 2nd Side length:"))
s3=int(input("Enter 3rd Side length:"))
Status=valid_triangle(s1,s2,s3)
if Status is True:
    print(f"Triangle with Sides {s1},{s2},{s3} is a Valid Triangle. ")
else:
    print(f"Triangle with Sides {s1},{s2},{s3} is a Not Valid Triangle. ")































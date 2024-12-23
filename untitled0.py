# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 19:08:10 2024

@author: admin
"""

# # a = input("enter the string : ")
# # vowels = "aeiou"
# # li = []


# # for i in a.lower():
# #     if i in vowels  and i not in li:
# #         li.append(i)
# # print(li)



# n = int(input("Enter Dictionary Count : "))
# dict1 ={}

# for i in range(0, n):
#     name = input("Enter name : ")
#     marks = int(input("Enter marks : "))
#     dict1[name] = marks

# print(dict1)
    
# dict1 = {} 
# sum = 0   


# for i in range(3):
#     n = int(input("enter the number : "))
#     dict1[i] = n
#     sum = sum + dict1[i]
    
# print(sum)

# a = "helloworld"
# count = 0
# # l1 = []
# dict1 = {}
# # dict1.update({1:2})
# for i in a :
#     if i in dict1: 
#         count = dict1.get(i) + 1
#         dict1.update({i:count})
#     else: 
#        dict1.update({i:1})
   
    
       
        
# # print(dict1)
#    3. Write a python program to extract element with frequency greater than k.
# Input - [ 4,6,4,3,3,4,3,4,6,6]
# # Output - [ 4,3,6]         

# list1 = [4,6,4,3,3,4,3,4,6,6] 
# l1= []
# n = 2

# for i in list1:
#     if i > n and i not in l1:
#         l1.append(i)
        
    
# print(l1) 



# # Write a python program to find the maximum number in the given list and print the index of the maximum element
# list1 = [1,2,3,4,5,2,1]
# max = list1[0]
# for i in list1:
#     if i > max:
#         max = list1[i]
# print("max element in index : " , list1.index(max))
  

# list1 = [7, 5, 5, 1, 6, 7, 8, 7, 6]
# l2 = []
# for i in list1:
#     if list1.count(i) == 1:
#         l2.append(i)
# print(l2)

# dict1 = {}

# n = int(input("Enter Dictionary Length"))
# for i in range(n):
#     name = input("Enter the name : ")
#     roll_no = int(input("Enter the Number : "))
#     dict1.update({ name : roll_no})
    
    
# while True:
#     print("1) get all values")
#     print("2) Add a new key-value pair in this dictionary and display the modified dictionary")
#     print("3) Delete a particular student's record from the dictionary")
#     print("4) Modify the name of an existing students.")
#     print("5) exit")
   
#     n = int(input("Enter the Choice : "))
    
#     match n :
#         case 1 :
#             for k,v in dict1.items():
#                 print(f"{ k  } : { v }")
#         case 2 :
#             name = input("Enter name : ")
#             number = int(input("Enter number : "))
#             dict1.update({ name : number})
#             print(dict1)
#         case 3 :
#             name = input("Enter name : ")
#             dict1.pop(name)
#             print(dict1)
            
#         case 4 :
#             name = input("Enter name : ")
#             number = int(input("Enter number : "))
#             dict1.update({ name : number})
#             print(dict1)
#         case 5 :
#             break

# a = "hello sushant how are you sushant ?"
# duplicate = a.split(" ")
# l1 = []
# for i in duplicate:
#     if i not in l1:
#         l1.append(i)
    
# a = str(l1)        
# print(a)
# print(type(a))


l1 = [1,2,3,4]
l2 = [["1,2,3"],["hello , buddy"] , ["kapse "],["radha"]]

dict1 = {1:'hello',2 : 5}
l1 = dict1.keys()
# for i in range(len(l1)):
#     dict1[l1[i]] = l2[i]



# for i,j in l1,l2:
#     dict1[i] = j
# print(dict1)
# for k , v in dict2.items():
#     dict1.update({k:v})
# print(dict1)
k = 5
# for i in l1:
#     if k == dict1[i]:
#         print("element " , k,"found at key : ", i)
 
if k in dict1.values():
    print("found")
else:
    print("Not Found")




































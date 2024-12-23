# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 23:03:11 2024

@author: admin
"""

# dict1 = {1:9,3:5,6:7,2:6}
# max1 = dict1[1]
# minkey = 1 

# for k , v in dict1.items():
#     if dict1[k] < max1:
#         max1 = dict1[k]
#         minkey = k
# print(minkey)


# 7. Write a Python program to count the number of strings from a given list of strings. The string length is 2 or more and the first and last characters are the same.
# Sample List = ['abc', 'xyz', 'aba', '1221']
# Expected Result : 2

# Sample_List = ['abc', 'xyz', 'aba','1221','sks']
# count = 0
# for i  in Sample_List:
#     if len(i) > 0 and i[0]==i[-1]:
#         count += 1
# print(count)

# Write a Python program to convert a list of characters into a string
# list1 = ['a','b','c','d']
# str2 = ""
# str1 = str(list1)
# print(str1)
# for i in list1:
#     str2 += i
# print(str2)

# Write a Python program to count the number of elements in a list within a specified range
# minrange = int(input("Enter Minimun range : "))
# maxrange = int(input("Enter Maximum range : "))
# list1 = [1,3,65,23,76,4,50,7,57,11]
# l2 = []
# for i in list1:
#     if i > minrange and i < maxrange :
#         l2.append(i)
# print(l2)    

# Write a Python program to create a list by concatenating a given list with a range from 1 to n.
# Sample Output : ['p1', 'q1', 'p2', 'q2', 'p3', 'q3', 'p4', 'q4', 'p5', 'q5']


# Sample_list = ['p', 'q']
# n =5
# add_no = 1
# l1 = []

# while add_no <= 5:
#     for i in Sample_list:
#         str1 = i + str(add_no)
#         l1.append(str1)
#     add_no += 1
# print(l1)
        
    
# Write a Python program to convert a list of multiple integers into a single integer.
# Expected Output: 113350
# Sample_list = [11, 33, 50]
# str1 = ""
# l2 = []

# for i in Sample_list :
#     str1 += str(i)
# l2.append(int(str1))
# print(l2)
    
#  Write a program to read 6 numbers and create a dictionary having keys EVEN and ODD. Dictionary's value should be stored in list. Your dictionary should be like:
# {'EVEN':[8,10,64], 'ODD':[1,5,9]}

# l1 = []
# l2 = []
# dict1 = {'EVEN' : l1,'ODD' : l2}

# for i in range(0, 6):
#     n = int(input("Enter The Number : "))
    
#     if n % 2 == 0:
#         l1.append(n)
#     else:
#         l2.append(n)
        
# print(dict1)

# Write a program to print all elements in a list those have only single occurrence.
# Example: if contents of list is [7, 5, 5, 1, 6, 7, 8, 7, 6].
# Your output should be:
# 1 8
# list1 = [7, 5, 5, 1, 6, 7, 8, 7, 6]
# list2 = []
# count = 0
# for i in list1:
#     if list1.count(i) == 1:
#         list2.append(i)
# print(list2)

# for i in list1:
#     if i not in list2 :
#         list2.append(i)
# print(list2)   



























# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 00:00:19 2024

@author: admin
"""

# Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples.
# Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]


Sample_List = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
# Sample_List.sort()
# print(Sample_List)
j = 1

for i, j in range(len(Sample_List)):
    print(Sample_List[i])











# # Define a function called 'last' that takes a single argument 'n' and returns the last element of 'n'
# def last(n):
#     return n[-1]

# # Define a function called 'sort_list_last' that takes a list of tuples 'tuples' as input
# def sort_list_last(tuples):
#     # Sort the list of tuples 'tuples' using the 'last' function as the key for sorting
#     return sorted(tuples, key=last)

# # Call the 'sort_list_last' function with a list of tuples as input and print the sorted result
# print(sort_list_last([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]))

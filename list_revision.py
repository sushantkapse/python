# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 10:54:04 2024

@author: admin
"""

# colors = [['Red'], ['Green'], ['Black']]
# for i in colors:
#     # print(i)

# Write a Python program to convert a list to a list of dictionaries.
# Sample lists: ["Black", "Red", "Maroon", "Yellow"], ["#000000", "#FF0000", "#800000", "#FFFF00"]
# Expected Output: [{'color_name': 'Black', 'color_code': '#000000'}, {'color_name': 'Red', 'color_code': '#FF0000'}, {'color_name': 'Maroon', 'color_code': '#800000'}, {'color_name': 'Yellow', 'color_code': '#FFFF00'}]
# using zip 

# # Sample lists
# color_names = ["Black", "Red", "Maroon", "Yellow"]
# color_codes = ["#000000", "#FF0000", "#800000", "#FFFF00"]

# # Using zip to combine the lists into pairs
# color_list = zip(color_names, color_codes)

# # Creating a list of dictionaries
# color_dicts = [{'color_name': color, 'color_code': code} for color, code in color_list]

# # Printing the list of dictionaries
# print(color_dicts)



# ------------------------------------------------------------------
# using normal

# Sample_lists1 = ["Black", "Red", "Maroon", "Yellow"]
# Sample_lists2 = ["#000000", "#FF0000", "#800000", "#FFFF00"]

# l3 = []
# dict1 = {}

# for i in range(len(Sample_lists1)):
#     dict1['colour name :']= Sample_lists1[i]
#     dict1['colour code :']= Sample_lists2[i]
#     l3.append(dict1)
# print(l3)


# my_list = [{'key': {'subkey': 1}}, {'key': {'subkey': 10}}, {'key': {'subkey': 5}}]

# -----------------------------------------------
Sample_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
l1 = []
for i in range(3):
    l1.append(Sample_list[i::3])
print(l1)

# -----------------------------
# l1 = ["red", "orange", "green", "blue", "white"]
# l2 =  ["black", "yellow", "green", "blue"]
# l3 = []

# for i in l1:
#     if i not in l2:
#         l3.append(i)
# print(l3)

# l3.clear()
# for i in l2:
#     if i not in l1:
#         l3.append(i)
# print(l3)


# # Import the 'Counter' class from the 'collections' module
# from collections import Counter

# # Define two lists 'color1' and 'color2' containing color names
# color1 = ["red", "orange", "green", "blue", "white"]
# color2 = ["black", "yellow", "green", "blue"]

# # Create Counter objects 'counter1' and 'counter2' for each list to count the occurrences of color names
# counter1 = Counter(color1)
# counter2 = Counter(color2)

# # Print the elements that are in 'counter1' but not in 'counter2' (Color1-Color2)
# print("Color1-Color2: ", list(counter1 - counter2))

# # Print the elements that are in 'counter2' but not in 'counter1' (Color2-Color1)
# print("Color2-Color1: ", list(counter2 - counter1))

# ---------------------------------------------------------------------

    
# original_list = [{'key1': 'value1', 'key2': 'value2'}, {'key1': 'value3', 'key2': 'value4'}]
# for i in original_list:
#     del[i['key1']]
    
# print(original_list)



# color1 = ["green", "orange", "black", "white"]
# isTr = None

# # Define another list 'color2' containing color names, with multiple occurrences of 'green'
# color2 = ["green", "green", "green", "green"]

# check = color1[0]
# for i in color1:
#     if i == check:
#         isTr = True
#     else:
#         isTr = False
# print(isTr)
    
num1 = [1, 3, 5, 7, 9, 10]
num2 = [2, 4, 6, 8]

num1[-1 :] = num2
print(num1)

num1[-1 ] = num2
print(num1)


# # Define a list 'num' containing integers
# num = [1, 2, 3, 4, 5]

# # Use the '*' operator in a print statement to unpack the elements of the list 'num' as separate arguments
# # This will print each element of the list separated by spaces
# print(*num)

# l1 = [3, 4, 0, 0, 0, 6, 2, 0, 6, 7, 6, 0, 0, 0, 9, 10, 7, 4, 4, 5, 3, 0, 0, 2, 9, 7, 1]

# l2 = []
# l3 = []

# for i in l1:
#     if i == 0:
#         l3.append(0)
#     else:
#         l2.append(i)
# l2.extend(l3)
# print(l2)


num = [[1, 2, 3], [4, 5, 40], [10, 11, 12], [7, 8, 9]]
sum1 = []
max_sum = 0

for i in num:
    currentsum = sum(i)
    
    if currentsum > max_sum:
        sum1 = i
        max_sum = currentsum
    
print(sum1)























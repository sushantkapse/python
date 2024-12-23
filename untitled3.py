# -*- coding: utf-8 -*-
"""
Created on Thu May  2 09:09:07 2024

@author: admin
"""

# l1 = [1,2,3,4]
# l2 = [12,13,14,15]

# ,

# import copy

# original_list = [[1, 2, 3], [4, 5, 6]]
# deep_copied_list = copy.copy(original_list)

# deep_copied_list[0][0] = 100

# print(original_list)        # Output: [[1, 2, 3], [4, 5, 6]]

# original_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# subset = original_list[:2]  # Shallow copy to create a view of the first two sublists

# # Modify the subset
# print(subset)  # Output: [[100, 2, 3], [4, 5, 6], [7, 8, 9]]
# subset[0][0] = 100

# # Original list is affected
# print(subset)  # Output: [[100, 2, 3], [4, 5, 6], [7, 8, 9]]


l1 = ["a","a","a","a","a","a","b","b","c","a","a","a","a"]
nl = []
# count = 1

# # for i in range(1,len(l1)):
# #     if l1[i]==l1[i-1]:
# #         count += 1
# #         print(l1[i])
# #     else:
# #         nl.append(l1[i-1])
# #         nl.append(count)
# #         count = 1
# nl.append(l1[-1])
# nl.append(count)
   
# print(nl)
     









i = 1
count = 1

def compressed(l1,i,count):
    
    if l1[i]==len(l1):
        return compressed(l1, i +1 , count)
    
    
    if l1[i]==l1[i-1]:
        count += 1
        
    else:
        nl.append(l1[i-1])
        nl.append(count)
        count = 1
    
nl.append(l1[-1])
nl.append(count)
   
print(nl)   
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

# def compress(input_list):
#     compressed_list = []
#     count = 1
#     for i in range(1, len(input_list)):
#         if input_list[i] == input_list[i - 1]:
#             count += 1
#         else:
#             compressed_list.extend([input_list[i - 1], count])
#             count = 1
#     compressed_list.extend([input_list[-1], count])
#     return compressed_list

# def decompress(compressed_list):
#     decompressed_list = []
#     for i in range(0, len(compressed_list), 2):
#         decompressed_list.extend([compressed_list[i]] * compressed_list[i + 1])
#     return decompressed_list

# def main():
#     input_list = ["A", "A", "A", "A", "A", "A", "A", "A", "A", "A", "A", "A", "B", "B", "B", "B", "A", "A", "A", "A", "A", "A", "B"]
#     print("Original list:", input_list)
    
#     compressed_list = compress(input_list)
#     print("Compressed list:", compressed_list)
    
#     decompressed_list = decompress(compressed_list)
#     print("Decompressed list:", decompressed_list)

# if __name__ == "__main__":
#     main()

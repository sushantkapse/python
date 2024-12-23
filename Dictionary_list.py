# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 13:15:17 2024

@author: admin
"""

dict1 = {0: 10, 4: 20, 2: 30,3 : 20}

# # print(sorted(dict1.items(),key =lambda x : x[1]),reverse= True )
# dict1.update({4:10})
# print(dict1)

# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50,6:60}
# dict4 = {}

# for i in (dic1,dic2,dic3):
#     dict4.update(i)
# # print(dict4)


# k = 1

# keys = dict4.keys()
# if k in dict4:
#     print("yes")
# else:
#     print("False")

# dict1 = {}

# for i in range(5):
#     dict1[i] = i * i
# print(dict1)

# d  = {10 : 10}
# dict1.update(d)
# print(dict1)

# res = {}
# for k ,v in dict1.items():
#     if v not in res.values():
#         res[k] = v
        
# print(res)
        
# dict2 ={}

# if len(dict2) > 0 :
#     print("true")
# else:
#     print("false")
 

# d1 = {'a': 100, 'b': 200, 'c':300}
# d2 = {'a': 300, 'b': 200, 'd':400}
# res = {}

# for i in d1:
#     if i in d2:
#         res[i] = d1[i] + d2[i]
#     else:
#         res[i] = d1[i]
# for i in d2:
#     if i not in res:
#         res[i] = d2[i]
# print(res)
   

# Sample_Data = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
# res = {}
# l1 = []

# for i in Sample_Data:
#     if i not in l1:
#         l1.append(i.)
# res["unique"]= l1
# print(res)
    


# Sample_data = {'1':['a','b'], '2':['c','d']}
# l1 = list(Sample_data.keys())

# # for k, v in Sample_data.items():
# #     for k1,v1 in Sample_data.items():
# #         if k1 != k:
# #             for i in v:
# #                 for j in v1:
# #                    print(i + j) 

# for i in range(len(l1)-1):
#     for elm1 in Sample_data[l1[i]]:
#         for j in Sample_data[l1[i+1]]:
#             print(elm1 + j)

# # Sample_data = {'1': ['a', 'b'], '2': ['c', 'd']}

# keys = list(Sample_data.keys())
# for i in range(len(keys) - 1):
#     for item1 in Sample_data[keys[i]]:
#         for item2 in Sample_data[keys[i + 1]]:
#             print(item1 + item2)


# my_dict = {'a': 500, 'b': 5874, 'c': 560, 'd': 400, 'e': 5874, 'f': 20}
# res = []

# res = sorted(my_dict.items(), key=lambda x :x[1],reverse = True)
# for i in res[:3]:
#     print(i[0])
    
# Sample_data = [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
# res = {}
# for i in Sample_data:
#     item = i['item']
#     amount = i['amount']
#     if item in res:
#         res[item] = res[item] + amount
#     else:
#         res[item] = amount
# print(res)

# Sample_string = 'w3resource'

# dict1 = {}
# for i in Sample_string:
#     if i in dict1:
#         dict1[i] += 1
#     else:
#         dict1[i] = 1
# print(dict1)

# # Create a list 'num_list' containing numbers.
# num_list = [1, 2, 3, 4]

# # Create an empty dictionary 'new_dict' and initialize 'current' to reference the same dictionary.
# new_dict = current = {}

# # Iterate through the numbers in 'num_list' using a for loop.
# for name in num_list:
#     # Create a nested empty dictionary under the 'current' dictionary with the current 'name' as the key.
#     current[name] = {}
    
#     # Update the 'current' reference to point to the newly created nested dictionary.
#     current = current[name]

# # Print the 'new_dict' dictionary, which is a nested structure with empty dictionaries.
# print(new_dict)



# num = {'n1': [2, 3, 1], 'n2': [5, 1, 2], 'n3': [3, 2, 4]}
# res = {}
# for k,v in num.items():
#    # v.sort()
   
#    # res[k]= v
#    res[k]= sorted(v)
# print(res)
    

# student_list = {'S  001': ['Math', 'Science'], 'S    002': ['Math', 'English']}
# res = {}
# for i,k in student_list.items():
    
#     str1 = ""
#     for j in i :
#        if j != " " :
#            str1 += j
#     print(str1)
#     res[str1] = k
# print(res)
       

# Sample_data =  {'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}
# res = {}

# res = sorted(Sample_data.items(), key=lambda x : x[1], reverse=True)

# for i in res[:3]:
#     print(i)


# # Create a dictionary 'dict_num' with keys and values.
# dict_num = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

# # Print a header for the output table.
# print("key  value  count")

# # Iterate through the key-value pairs in 'dict_num' using the 'enumerate' function.
# # The 'enumerate' function assigns a count starting from 1 to each pair and unpacks them as (count, (key, value)).
# for count, (key, value) in enumerate(dict_num.items(), 1):
#     # Print the key, value, and count in a formatted table.
#     print(key, '   ', value, '    ', count) 


# Create a dictionary 'student' with key-value pairs representing a student's information.
# student = {
#   'name': 'Alex',
#   'class': 'V',
#   'roll_id': '2'
# }

# a = student.keys() >= {'class','ok'}
# print(a)
# b = student.keys() >= {'class','name'}
# print(b)

# dict1 =  {'Alex': ['subj1', 'subj2', 'subj3'], 'David': ['subj1', 'subj2']}

# l1 = dict1.values()
# count= 0
# for i in l1:
#     for j in i:
#         count+= 1
# print(l1)
# print(count)

# dict1 = {'x' : [11, 12, 13, 14, 15, 16, 17, 18, 19],
#          'y': [21, 22, 23, 24, 25, 26, 27, 28, 29],
#          'z': [31, 32, 33, 34, 35, 36, 37, 38, 39]}
# for k ,v in dict1.items():
#     print(v[4])














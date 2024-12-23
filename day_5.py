# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 10:11:38 2024

@author: admin
"""

# list comprehenssin

# l1  = [1,2,3,4,5]
# l2= []
# for i in l1:
#     s = i * i
#     l2.append(s)
    
# l3 = [i*i for i in l1]

# print(l3)


f = ['apple','banana','hello']

# # if only if then after for loop and :
# #     if if else then before for loop

# f1 = [x for x in f if 'a' in x]
# print(f1)

# f2 = [x if x != 'banana' else 'orange ' for x in f ]
# print(f2)



# refrence variable 

# if l2 is define then this not change by assign operator
# shallow copy and deep copy
# xerox 
# copy functon


l1 = [1,2,3,4]
l2 = []
print(id(l2))
l2 = l1
l2[2] = 50
print("l1 ", l1,id(l1))
print("l2 : ",l2,id(l2))

# l3 = l1.copy()
# l3[1] = 40

# print("l1 ", l1,id(l1))
# print("l3 : ",l3,id(l3))


# import copy 
# l4 = copy.deepcopy()....................?





# Map1 like iterator function in java 

# in map we pass function as a paramaeter

# map return map object

# zip1

# diffrence between for and map1

# inuilt function
# test = list(map(str.upper, f))
# print(test)


# # if inly map then it return object1
# st = map(str.upper, f)
# print(st)


# def addition(n):
#     return n + n
# l1 = [1,2,3,4]
# # callback function
# l2 = list(map(addition,l1 ))            
# print(l2)

# we pass n number of sequence in map 

# iterattion 
# 1) for loop
#     2) comprehenssion
#     3) map function
    























# ----------------------------------


# dictionary

# dict() --> pass in tuple
# type()
# get()
# if key is not in dict and we use get() then it return None
# keys()
# values()
# items()
# update({}) ---> key and value -- if key is present update the value
# setdefault() ----> key and value if key is present not update value set previous value 
# clear()
# pop()
# del()
# sorted() - . on keys sort and return keys



# dict1 = {}
# print(type(dict1))
# n = int(input("Enter Dictionary Length"))
# for i in range(n):
#     name = input("Enter the name : ")
#     telephone = int(input("Enter the Number : "))
#     dict1.update({ name : telephone})
    
    
# def shown():
#     print("1. look telephone")
#     print("2. add new name")
#     print("3. edit telephone numbet")
#     print("4. delete entry")
#     print("5. print phone directory")
#     print("6. quit")
  
    
    
# while True :
#     shown()
#     n = int(input("Enter your Chouce : "))
    
#     match n :
#         case 1 :
#             name = input("Enter name : ")
            
#             print( dict1[name])
#             print(dict1)
#         case 2 : 
#             name = input("Enter name : ")
#             number = int(input("Enter number : "))
#             dict1.update({ name : telephone})
#             print(dict1)
#         case 3 :
#             name = input("Enter name : ")
#             number = int(input("Enter number : "))
#             dict1.update({ name : telephone})
#             print(dict1)
#         case 4:
            
#             name = input("Enter name : ")
#             dict1.pop(name)
#             print(dict1)
#         case 5 :
#             print(sorted(dict1))
            
#         case 6 : 
#             break

    
    


# dict1 = { 1 : ['.',',','?','!',':'] , 2 : ['A','B','C'], 3 : ['D','E','F'], 4 : ['G','H','I'], 5 : ['J','K','L'] ,6 : ['M','N','0'], 7 :['P','Q','R','S'], 8 : ['T','U','V'] , 9 : ['W','X','Y','Z'], 0 : [ ' ']}

# name = "Hello World!"
# ans = ""

# for i in name :
#     for k,v in dict1.items():
#         if i.upper() in v:
#             ans+= str(k) * (v.index(i.upper())+1)
# print(ans)
        




dict1 = {0:'zero' , 1:'one', 2: 'two',3:'three',4:'four',5:'five', 6:'six',7:'seven',8:'eight',9:'nine',
          20 : ' twenty ', 30 : 'thirty', 40 :'fourty', 50:'fifty', 60 : 'sixty', 70:'seventy',80:'eighty', 90:'ninety',
          10 :'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen'}
# # dict2 = {3 : 'hundread', 4:'thousand'}

   
            
ans = ""
power  = 0
number = int(input("enter the number : "))
fd = number // 100
a = number % 100
while number > 0:
    rem = number % 10 
    final_int = rem * pow(10, power)
    if final_int < 10:
        if final_int != 0:
            ans = dict1.get(final_int) + ans
            # print(ans,1)
        
    elif final_int > 9 and final_int < 20:
        ans = dict1.get(a) 
        
        # print(ans,2)
    elif final_int > 19 and final_int < 100:
        ans = dict1.get(final_int) + " "+ ans
        # print(ans,3)
    elif final_int > 99:
        ans = str(dict1.get(fd)) + " hundread " + ans 
        # print(ans)
        
        
    power += 1
    number = number // 10
            
    
print(ans)
    
# print(300//100)









            
        
    



































 

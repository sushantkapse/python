# -*- coding: utf-8 -*-
"""
Created on Sat Apr 20 10:17:10 2024

@author: admin
"""

# Tuple No modification allowed like list 
# Tuple is immutable we cant add value and delete valu and reassingn value1
# max() = homogenous numbeers only
# min() = homogenous numbeers only


# tuple1 = (1,2,3)
# tuple2 = (2,1,4)

# dict1 = dict(zip(tuple1,tuple2))
# print(dict1)


# =================================================
# set = no index value
# unique element
# unorder . sequence not maintain
#  modification not allowed
# s1 = {1,'2'}
# s2 = {1,'2',3}
# print(s1|s2)

# ===========================================================

# call by refrence : pass value by its address ,,   fun() it is by default
# actual argument = in function call
# formal parameter = in function defination ,  copy od actual agument

# method : member of class is 
# function = block of code  perform particular code 


# why we can`t make global vaiable = it can increase space complexity , stack overflow 

# disadvantage of function 
# when function call over it come back in main 

# match function in that we can use also string in switch we cant use string 



# balance = 1000

# # n = int(input("Enter Your Choice : "))

# def deposit():
#     global balance
#     amount = int(input("Enter amount to add : "))
#     balance += amount
#     print("Ypur balance is ", balance)
    
# def withdrawn():
#     global balance
#     amount = int(input("Enter amount to withdrawn : "))
#     balance -= amount
#     print("Ypur balance is ", balance)
    

# def shown():
#     print("1)Deposit Money ")
#     print("2)Withdrawl Money ")
#     print("1) quit ")
    
    
# while (True):
#     shown()
#     n = int(input("Enter Your Choice : "))
#     match n:
#         case 1 :
#             deposit()
#         case 2 :
#             withdrawn()
#         case 3 :
#             break
        
    
  # multiple assingnment allowe d in ptthon and in pyhotn we can return n number of  values in function
  
# if we want a specific datatype then it will be by 
# x = 1
# y = 1
# def test (x,y):
#     x += 1
#     y += 2
#     return x,y
# x,y = test(x, y)
# print(x,y)


# def sum1(a,b):
#     print(1,2)
    
# def sum1(a,b,c):
#     print(1,2,3)
    
# sum1(1,2,3)
# sum1(1,2)


# functiona overloading concept in not allowed in python
# function overloading is achieve by var-arg

# def sum1(a,*b):
#     sum = 0
#     print (a)
   
    
# sum1(1,2)
# print("---")
# sum1(1,2,3)
# print("---")
# sum1(1,2,3,4)

# here * means  for sequence   

# var arg method

def fun():
    print("Hello Buddy !")
    
def ok():
    print("kaise ho..?")

count = 0

def sentence_most_string_(l1):
    l2 = []
    l3 = []
    for i in l1:
        
        if l1.count(i) > 1:
            l2.append(i)
    # print(l2)
    
    for i in l2:
        if i not in l3:
            l3.append(i)
    if len(l3) > 0:
        for i in l3:
            print(i)
    else:
        print("No element Commom")
        
   
    
    
        

        






































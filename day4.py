# # -*- coding: utf-8 -*-
# """
# Created on Sun Apr  7 12:05:04 2024

# @author: admin
# """

# # mylist = []
# # # print(mylist)
# # c = len(mylist)
# # print(c)

# # # empty list 
# # mylist1 = []
# # a = len(mylist)
# # print(a)

# """
# append = at last
# insert(2,10) = at 2th index 100 will add
# remove()
# pop()
# li + l2 = list concatetion
# extend()
# zip()


# """


# # mylist = []
# # n = int(input("Enter How many element you want :"))

# # for i in range(n):
# #     element = input("Enter value : ")
    
# #     if element == "END" :
# #         break 
# #     mylist.append(element)
    
# # print("first half element")

# # for i in range(0, len(mylist)//2):
# #     print(mylist[i])



# # list1 = [1,23,5,1,5,6,4]
# # number = 0
# # n = len(list1) 

# # for i in range(0, n):
    
    
# #     number = list1[i]
# #     for j in range(i+1,n):
# #         if list1[j] == number:
# #             list1.pop(j)
            
        
             
        
# # print(list1)


# # l1 = []

# # for i in range(0, 3):
# #     name = input("enter city")
# #     t_min = input("min")
# #     t_max = input("max")
# #     l = [name,t_min,t_max]
# #     l1.append(l)
# # print(l1)
# import random

# list1 = [['AAA01',135],['BBB01',87],['CCC01',188],['DDD01',109]]




# while True:
#     id = input('Enter the id :')
#     a = False
#     score = random.randint(50, 200)
    
#     if id == "xxx":
#         break
    

    
#     for i in range(len(list1)):
#        if list1[i][0] == id:
#            a = True
#            if list1[i][1] <= score:
#                list1[i][1] = score
#            break
                
#     if a == False:
#        list1.append([id, 0])
     
#     print(list1)

        
# print(list1)





# #



# list1 = [['AAA01', 135], ['BBB01', 87], ['CCC01', 188], ['DDD01', 109]]
# id = input('Enter the id: ')

# a = False

# for i in range(len(list1)):
#     if list1[i][0] == id:
#         a = True
#         break

# if not a:
#     list1.append([id, 0])

# print(list1)




# list1 = [1,2,3,4,1,2]
# list2 = []
# for i  in list1:
#     if i not in list2:
#         list2.append(i)


# print(list2)

# def print_pattern(rows):
#     num = 1
#     for i in range(1, rows + 1):
#         for j in range(i, 0, -1):
#             print(num, end=" ")
#             num += 1
#         print()

# print_pattern(4)


# num = 1

# for i in range(1,4+1):
  
#     for j in range(i):
        
#         print( num, end=" ")
#         num -= 1 
     
#     num = num + i    
    
#     print()








dict1 = {1:'hello', 2: 'worlds' }
print(dict1)
















































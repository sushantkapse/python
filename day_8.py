# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 10:20:54 2024

@author: admin
"""

# keyword argument = not required to learn sequence 

# default argument 

# kwargs = return values in pair i.e in dictionary 
# inline function = 
# lambda

# def fun(name, *n,**marks):
#     print("name : ",name)
#     print("insem marks : ",n)
#     print(marks)
# fun("sushant", 9,6,8,2,6,3, History = 10, Geography = 8, Maths = 9) 


# def books(**books):
    
# #     l1 = list(books.values())
# #     l2 = list(books.items())
# #     dict1
#     print(sorted(books.items(),key=lambda kv : kv[1]))
    
# #     print(l1)
# #     l1.sort()
# #     for i in l1:
       
        
        

# # books(history = 10,geography = 2,politics = 12,Economics = 5)
# library = {}
# def add_book(library, key, **book_details):
#     library[key] = book_details

# # def display_books_by_cost(library):
# #     sorted_books = sorted(library.items(), key=lambda x: x[1]['cost'])
    
# #     print("Books sorted by cost (ascending):")
# #     for key, book in sorted_books:
# #         print(f"{key}: {book}")


# add_book(library, "book1", title="Python Programming", cost=30)
# add_book(library, "book2", title="Data Structures", cost=25)
# add_book(library, "book3", title="Machine Learning", cost=40)
# add_book(library, "book4", title="Artificial Intelligence", cost=50)
# print(library)

# # display_books_by_cost(library)






# ====================================================================


# import day_7

# # # ok()

# sentence = "hello sushant kapse "
# sentence_list = sentence.split(" ")

# day_7.sentence_most_string_(sentence_list)



# # callback function


# n = 10
# l1 = []
# for i in range(n):
#     if n % i == 0:
#         l1.append(i)
# print(i)

l1 = []

def isPrime(n):
    if n <= 1:
        return False
    for i in range(2,n):
        if n % i == 0:
            
            return False
    return True 
           

def prime_number_range (n):
  
    for i in range(1,n):
        if isPrime(i):
            l1.append(i)
            
   
    
prime_number_range(10)

n  = int(input("Enter Number : "))

def prime_factors(n):
    l2 = []
    for i in l1:
        while n % i == 0:
            n = n // i
            l2.append(i)
    
    print(l2)
print("Prime factors of number : ", n)
prime_factors(n)
    

         


























        
        

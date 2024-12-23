# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 10:09:54 2024

@author: admin
"""

# c= procedure oriented programming -> no security
# procedure of 
# modification is not easy

# object =  a real world entity -> need security and covered in opps = >Data + Object 
# modification easy
# emphasize on data
# data is hidden cant be acces 
# bottom-Up approach  = main is at lower and from main control is go upward 

# featurs , characteristics, real life , 4 pillars

# common =  static1

# encapsulation = class is imlementation , wrapping of data, binding and , getters and setters
# abstraction = hidind data and showing essential features
# inheritence = 
# polymorphism = only runtime in python
# upcasting and downcasting

# class1

# self = parameter, every method in class have self parameter , self is like pointer like this in java
# whenevr we use self then it is instance variable
# but in java this is compulsary and self cha nav kahihi asu shakata
# instance variable = self current object reference 


# class emp :
#     name = ""
#     sal = 0
#     def getdata(self):
#         self.name - input("name : ")
#     def putdata(self):
#         print(self.name)
        
        

# e = emp()  memory initialization occur name = null 

# e.getdata() here also memory call and values given
# so we use constructor = only one memory call above two times memory call
# e.putdata()


# whenever we create object the instance variable for that object created

# in java we use array of object for multiple object1
# in python we use list 





# Develop a program having data members author, title, price and stock position. Define a method to accept information from user and display information for 3 books.



# class Book:
#     def getdata(self):
#         self.author = input("Enter Author Name : ")
#         self.title = input("Enter Title Name : ")
#         self.price = int(input("Enter Price : "))
#         self.stock_posiion = int(input("Enter stock : "))
        
#     def display(self):
#         print("Author Name : ", self.author)
#         print("Title Name : ", self.title)
#         print("Price : ", self.price)
#         print("Stock Postion : ", self.stock_posiion)
        
# book = []

# for i in range(3):
#     b = Book()
#     b.getdata()
#     book.append(b)
# for i in book:
#     print("-------------")
#     i.display()



# whenever we create an object that time dictionary is created for object and we have (e.__dict__) then we 
# can acces dictionary for that

# vars(e) = 
# vars()




# in java static variable is associated to every object 
# here is class variable
# we can access it by class name not need  SELF parameter


# class test:
#     total_amount = 0
#     def getdata(self):
#         self.amt = int(input("Enter amount : "))
#         test.total_amount += self.amt
#     def putdata(self):
#         print("amoutn :", self.amt)
#     def display(self):
#         print("final : ", test.total_amount)
# t1 = test()
# t2 = test()
# t3 = test()
# t4 = test()

# t1.getdata()
# t2.getdata()
# t3.getdata()
# t4.getdata()


# t1.putdata()
# t2.putdata()
# t3.putdata()
# t4.putdata()

# t1.display()
        


# Define a class student having roll_no, name and marks of English, maths, science 

# class Student:
#     English = 0
#     science = 0
#     maths = 0
#     avg_English = 0
#     avg_science = 0
#     avg_maths = 0
#     sum_English = 0
#     sum_science = 0
#     sum_maths = 0
    
    
    
#     def getdata(self):
#         self.roll_no = int(input("Enter Roll No : "))
#         self.name = input("Enter Name : ")
#         self.English = int(input("Enter English Marks : "))
#         self.science = int(input("Enter Science Marks : "))
#         self.maths = int(input("Enter Maths Marks : "))
#         Student.sum_English += self.English
#         Student.sum_maths += self.maths
#         Student.sum_science += self.science
#         print()
        
#     def display_student_data(self):
#         print("Student Name : ", self.name)
#         print("Student Roll No. : ", self.roll_no)
#         print("English Marks : ",self.English)
#         print("science Marks : ",self.science)
#         print("maths Marks : ",self.maths)
        
#         avg = (self.English +self.science + self.maths)/3
#         print("average is : ",avg)
        
#         print("---------------------------")
        
    
#     @staticmethod    
#     def average_subject(number):
       
#         avg_English = Student.sum_English / number
#         avg_science = Student.sum_science / number
#         avg_maths = Student.sum_maths / number
        
#         print("Science : ",avg_science)
#         print("Maths : ",avg_maths)
#         print("English : ",avg_English)
        
 
        
# number = int(input("How Many Student in Class"))
# for i in range (number):
#     s = Student()
#     s.getdata()
#     s.display_student_data()

# Student.average_subject(number)     
        
        




# static method = we need to use only @staticmethod decorater in that static method not need to give self as parameter
# static method only call static member






# private method and private variable
# in python public private protected keyword not present 


# we cant call private method directly we need to call it through public method 
# it can implement ny __fun() and for acces alos two underscore required and self paramaeter is need , 
# self is not parameter it only a reference
# outside class we cant private members
# class test:
#     __a = 0
#     b = 0
#     def __init__(self):
#         print("constructor")
#     def __fun(self):
#         print("hello")
#         self.__a = 200
#     def display(self):
#         self.__fun()
#         print("**********")
#         print(self.__a ,"  ", self.b)
#     def __del__(self):
#         print("hello the end")
        
# t1 = test()
# t1.b = 300
# t1.display()
# t = test()
# t.display()

# constructor = build your object ,  whenever object is create at that time it hav value 
# __int__ = init is shortform of initializayion
# initialize your ininstance values
# never return any value

# destructor = destroy object when we object no longer use = def __del__
# del = destroy object forcefully either it is used or not1 ,,,,  not any parameter only self
# in java we cannot delete only one property we have to deleter whole object but here we delete only one property by del keyword


# class retail:
#     def __init__(self,item_number,charge = 75):
#         self.ans = charge * item_number
#     def answer(self):
#         print("charges are : ",self.ans)
        
        
# a = retail(2)
# a.answer()


# Define a class that can describe a hotel It should have members that initialize the name, address, grade, average room charges and number of rooms.
# Write function to perform the following operations:
# a)	To print out hotels of a given grades in order of charges.
# b)	To print out hotels with room charges less than a given values


class hotel:
    def __init__(self,name,address,grade,average_room_charges,room_no):
        self.name = name
        self.address = address
        self.grade = grade
        self.average_room_charges = average_room_charges
        self.room_no = room_no

l1 = []
for i in range(2):
    name = input("enter name : ")
    address = input("enter name : ")
    grade = input("enter name : ")
    average_room_charges = int(input("enter name : "))
    room_no = int(input("enter name : "))
    
    h= hotel(name, address, grade, average_room_charges, room_no)
    l1.append(vars(h))
    


print(l1)

   
        

def sort_by_grade(l1):
    res = sorted(l1 , key=lambda x :x['grade'])
    for i in res:
        for k , v 
    
sort_by_grade(l1)




























        
        
        
        





























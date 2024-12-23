# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 13:43:31 2024

@author: admin
"""

dict1 = {1 : ['A','J','S'], 
         2 : ['B','K','T'], 
         3 : ['C','L','U'], 
         4 : ['D','M','V'], 
         5:  ['E','N','W'], 
         6 : ['F','O','X'], 
         7 : ['G','P','Y'], 
         8 : ['H','Q','Z'], 
         9 : ['I','R'], 
         }

lucky_number_meaning = {
    1: "Natural leaders",
    2: "Natural peacemakers",
    3: "Creative and optimistic",
    4: "Hard workers",
    5: "Value freedom",
    6: "Carers and providers",
    7: "Thinkers",
    8: "Have diplomatic skills",
    9: "Selfless and generous"
}



def sum_of_digit(number):
    sum = 0
    while number > 0:
        
       
        rem = number % 10
        sum += rem
        number = number // 10
        
    return sum


a = "Wiseman"
def word_number(a):
    sum = 0
    for i in a:
        for k , v in dict1.items():
            if i.upper() in v:
                sum += k
               
    if sum > 9:
        sum = sum_of_digit(sum)
    return sum
# word_number(a)

name = input("Enter Your Name : ")
l1 = []


def lucky_number(name):
    lucky_number1 = 0
    l1 = name.split(" ")
    for i in l1:
        lucky_number1 += word_number(i)
    if lucky_number1 > 9:
        lucky_number1 = sum_of_digit(lucky_number1)
    return lucky_number1
        
print("Your Name is : ",name)
ln = lucky_number(name)
print("Your Lucky Number is : ",ln )
print("Your Lucky Number Meaning : ", lucky_number_meaning[ln])

    
































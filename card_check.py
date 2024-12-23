# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 17:24:11 2024

@author: admin
"""


from datetime import datetime, timedelta

def sum_of_digit(number):
    sum = 0
    while number > 0:
        
        digit = number % 10
        sum = sum + digit
        number = number // 10
    return sum
        

def is_Valid (number):   
    sum = 0
    if len(number) >= 8:
        checkdigit = int(number[-1])
        seven_no = number[0:7]
        reverse_seven = seven_no[::-1]
        
        
        sum = 0
        no = 0
        for i in range(0,len(reverse_seven)):
            # print(reverse_seven[i])
            
            if (i % 2 == 0):
                
                no = int(reverse_seven[i]) * 2
                
                if int(no) > 9:
                    no = sum_of_digit(no)    
            else:
                no = int(reverse_seven[i])
            sum = sum + no
        sum += checkdigit
        if sum % 10 == 0:
            print("card is valid")
        else:
            print("card is not valid")
    else:
       print("card no does contain only 8 digit")
        

def date_check(date):    
    expiry_date = date + timedelta(days=365)   
    current_date = datetime.today()
       
      
    if current_date > expiry_date:
           return False
    else:
           return True
 
                
name = input("Enter Customer Name : ")
postcode = int(input("Enter Customer postcode :"))
card_issue_date = input("Enter issues date in format (DD-MM-YYYY): ")
date = datetime.strptime(card_issue_date, ("%d-%m-%Y"))
card_no = int(input("Enter Card Number : "))
card_no_str = str(card_no)

print("-------")

print("Name : ", name)
print("Postcode : ",postcode)
print("Card no. is : ",card_no)
print("card issue date : ",date.strftime("%d-%m-%Y"))
if (date_check(date)):
    print("Expiry Date is valid")
    
    is_Valid(card_no_str)
    
else:
    print("Expiry date is not valid")
 

  
         
            
        

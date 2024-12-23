# -*- coding: utf-8 -*-
"""
Created on Fri Apr 12 18:24:49 2024

@author: admin
"""




def password_check():
    password = input("Enter the password : ")
    if len(password) >= 8 and len(password) <= 24 :  
        if password_character(password):
            score = password_score(password)
            print("Your Password Score is : ", score)
            password_category(score)
            
        else:
            print("Please Enter Valid Characters")
    else:
        print("invalid length")
            

        
    

list2 = ['!','%','$','^','&','*','(',')','-','_','=','+']




def password_character(password):
    for i in password:
        if i in list2 or i.isalnum():
            return True
        else:
            return False
 
    
 
    
def querty_layout(password,score):
    new_password = password.lower()
    querty_list = ['qwertyuiop','asdfghjkl','zxcvbnm']
    for i in range(len(new_password)-2):
        letter_1 = new_password[i]
        letter_2 = new_password[i + 1]
        letter_3 = new_password[i + 2]
        
        
        if (letter_1 in querty_list[1] and letter_2 in querty_list[1] and letter_3 in querty_list[1]) or (letter_1 in querty_list[0] and letter_2 in querty_list[0] and letter_3 in querty_list[0]) or (letter_1 in querty_list[2] and letter_2 in querty_list[2] and letter_3 in querty_list[2]) :
            score -= 5

    return score
    
           
      
        
 
def password_score(password):
    score = len(password)
    capital = False
    small = False
    digit = False
    list2_item = False

    for i in password:
        if not capital and 'A' <= i <= 'Z' :
            capital = True
            score += 5
    
        if not small and 'a' <= i <= 'z':
            small = True 
            score += 5
               
        if not digit and '0' <= i <= '9':
            digit = True
            score+= 5
             
        if not list2_item and i in list2:
            list2_item = True
            score += 5
                
    if capital and small and digit and list2_item:
        score += 10
                  
    if password.isalpha(): 
        score -= 5
        
    if password.isdigit():
        score-= 5
        
    if password in list2:
        score-= 5
        
    modified_score =  querty_layout(password, score)
    
    return modified_score


def password_category(score):
    if score > 20:
        print("password is strong")
    elif score <= 0:
        print("password is weak")
    



import random

def generate_password():
    
    password = ""
    
    while password_score(password) < 20:
        
        n = random.randint(8, 12)
        for i in range(n):
            case = random.randint(1, 4)
            match case :
                case 1 :
                    pos = random.randint(65, 90)
                    password += chr(pos)
                case 2 : 
                    pos = random.randint(97, 122)
                    password += chr(pos)
                case 3 :
                    pos = random.randint(48, 57)
                    password += chr(pos)
                case 4:
                    a = random.choice(list2)
                    password += a
        print("Your Password is : ", password)
        score = password_score(password)
        print("Your Password Score is : ", score)
        password_category(score)



def shown():
    print("1. Check Password Score")
    print("2. Generate Password")
    print("3. Quit")



while True:
    shown()
    n= int(input("Enter Your Choice : "))
    match n :
        case 1 :
            password_check()
            
        case 2 :
            generate_password()
            
            
        case 3 :
            break
            
        case _ :
            print("Enter Valid Choice")
            
    print("------------")
            








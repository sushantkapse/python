# -*- coding: utf-8 -*-
"""
Created on Fri May  3 19:06:33 2024

@author: admin
"""

# An interactive calculator
# Exercise
# You're going to write an interactive calculator! User input is assumed to be a formula that consist of a number, an operator (at least + and -), and another number, separated by white space (e.g. 1 + 1). Split user input using str.split(), and check whether the resulting list is valid:

# If the input does not consist of 3 elements, raise a FormulaError, which is a custom Exception.
# Try to convert the first and third input to a float (like so: float_value = float(str_value)). Catch any ValueError that occurs, and instead raise a FormulaError
# If the second input is not '+' or '-', again raise a FormulaError
# If the input is valid, perform the calculation and print out the result. The user is then prompted to provide new input, and so on, until the user enters quit.



class FormulaError(Exception):
    pass

try:
    n = input("Enter Input : ")
    
    if len(n) != 3:
        raise FormulaError 
    l1 = n.split()
    try :
        
        n1 = float(n[0])
        n2 = float(n[2])
   
        if isinstance(n1, float) and isinstance(n2, float):
            operator = n[1]
            match operator :
                
                case '+':
                    c = n1 + n2
                    print(c)
                case '-' :
                    print(n1-n2)
                case _:
                    raise FormulaError

  
    except ValueError:
        print("Enter Proper values")
        
except FormulaError:
    print("Enter Valid Input")


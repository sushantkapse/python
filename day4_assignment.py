# -*- coding: utf-8 -*-
"""
Created on Fri Apr 12 14:18:55 2024

@author: admin
"""

import datetime
monthly_avg = []
year = 2024

hot_temp = 34
cold_temp = 29

hot_month = []
cool_month = []

for i in range (1,13):
    date = datetime.date(year,i,1)
    month = date.strftime("%B")
    min_temp = int(input(f"Enter minimum temprature for {month} : "))
    max_temp = int(input(f"Enter maximum temprature for {month} : "))
    
    monthly_avg.append([month,min_temp,max_temp])
    
for i in monthly_avg:
    print(f" {i[0]} --- {i[1]} --- {i[2]}", end=" ")
    print()
    
    
    

for i in monthly_avg:
    if i[1] + i[2] < cold_temp :
        cool_month.append([i[0],(i[1]+i[2])/2])
    elif i[2] + i[1] > hot_temp :
        hot_month.append([i[0],(i[1]+i[2])/2])
        
print("---- Hot Moths -----")
for i  in hot_month:
    print(i , end=" ")
    
    
print("---- Cold Moths -----")
for i  in cool_month:
    print(i , end=" ")
     


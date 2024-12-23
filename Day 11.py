# -*- coding: utf-8 -*-
"""
Created on Sun May  5 09:58:16 2024

@author: admin
"""

# with open :
    
# tell() = tell cursor position 
# seek() = move cursor

# with open("test.txt","r") as f1:
#     rec=f1.readline()
#     while rec!="":
#         li=rec.split(" ")
#         f2 = f1.move(12)
#         print(f2.tell())
#         rec=f1.readline()

import csv

# csv file ----------------comma separated value
def getdata():
    # need to give file mode but by defaut it is read
    with open("E:\python\zoo.csv") as f1 :
        records = csv.reader(f1)
        print(type(records))
        for i in records:
            print(i)
            
def putdata():
    with open("E:\python\zoo.csv","a") as f1 :
        write = csv.writer(f1)
        write.writerow(['Lion',1023,450])
# putdata()
getdata()
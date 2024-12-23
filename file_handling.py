# with open("test.txt","a")as f1:
#     for i in range(3):
#         name=input("Enter Name:")
#         fees=eval(input("Enter Fees:"))
#         f1.write(name+" "+str(fees)+"\n")
# print(f1.closed)

with open("test.txt","r") as f1:
    rec=f1.readline()
    while rec!="":
        li=rec.split(" ")
        if int(li[1])<=50000:
            print("Name:",li[0], "Fees:",li[1])
        rec=f1.readline()

f1 = open("test.txt","r")
rec = f1.read()
print(rec,type(rec))

# f1 = open("day10.txt","w")
# # cursor is at begining
# # w = create new file every time 
# f1 = f1.write("My name is sushant")


# for appending data in file = " a "
# f1 = open("day10.txt","a")
# f1.write("saheb....\n")
# # \n = new line
# f1.write("avdhut .....")
# f1.close()
# print(f1.closed)


# with open("test.txt","a") as f1:
#     f1.write("hello")
# print(f1.closed)

# write function takes only one argument

# with open("test.txt","a") as f1:
#     for i in range(5):
#         name = input("enter name : ")
#         fee = int(input("Enter fee :"))
        
#         f1.write(name + " " + str(fee) + "\n")
#         # str because only take 1 argument 
# print(f1.closed)


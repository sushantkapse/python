# class student:
#     def getdata(self):
#         self.name=input("Enter name:")
#         self.rollno=int(input("Enter roll no:"))
#     def putdata(self):
#         print("Name:",self.name, "Roll No:",self.rollno)
# class test(student):
#     def get_marks(self):
#         self.s1=int(input("Enter marks:"))
#         self.s2=int(input("Enter marks:"))
#         self.s3=int(input("Enter marks:"))
#     def display(self):
#         total=self.s1+self.s2+self.s3
#         print("Percentage:",total/3)
# t1=test()
# t1.getdata()
# t1.putdata()
# t1.get_marks()
# t1.display()


#to make private method write __ before method name and call it in public method.

class student:
    def getdata(self):
        self.name=input("Enter name:")
        self.rollno=int(input("Enter roll no:"))
        self.__putdata()
    def __putdata(self):
        print("Name:",self.name, "Roll No:",self.rollno)
class test(student):
    def get_marks(self):
        self.s1=int(input("Enter marks:"))
        self.s2=int(input("Enter marks:"))
        self.s3=int(input("Enter marks:"))
    def display(self):
        total=self.s1+self.s2+self.s3
        print("Percentage:",total/3)
class sports(student):
    def get_sports(self):
        self.sp_name=input("Enter sports name:")
        self.grade=input("Enter grade:")
        print("Sports name:",self.sp_name, "Grade:",self.grade)

t1=test()
s1=sports()
t1.getdata()
#t1.putdata()
t1.get_marks()
t1.display()
s1.get_sports()
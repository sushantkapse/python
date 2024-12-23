# class A:
#     def __init__(self,n):
#         self.a=n
#     def put_a(self):
#         print("Class A:",self.a)

# class B:
#     def __init__(self,n):
#         self.b=n
#     def put_b(self):
#         print("Class B:",self.b)
# class C(A,B):
#     def __init__(self,n,m,o):
#         A.__init__(self,m)# this is used for multiple parent
#         B.__init__(self,o)
#         #super().__init__(m)= this used in simgle level inheritance so it will only call in parent class constructor
#         self.c=n
#     def put_c(self):
#         print("Child class:",self.c)
# c1=C(100,200,300)
# c1.put_a()
# c1.put_b()
# c1.put_c()


class A:
    def get(self):
        print("welcome")
    def display(self):
        print("Bold")
class B(A):
    def get_data(self):
        print("welcome Class B")
    def display(self):
        print("GIF")

b1=B()
b1.get()
b1.get_data()
b1.display()
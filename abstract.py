from abc import ABC,abstractmethod
# class side(ABC):
#     @abstractmethod
#     def no_of_side(self):
#         pass

# class B(side):
#     def put(self):
#         print("upload")
#     def no_of_side(self):
#         print("3 side")

# b=B()
# b.put()
# b.no_of_side()

class Loader(ABC):
    @abstractmethod
    def loadOS(self):
        pass

class Device:
    def data(self):
        self.vendorName=input("Enter your Vender NAme:")
        self.ramsize=int(input("Enter ram Size:"))
        self.osversion=input("Enter os version:")
        print(f"Vender Name: {self.vendorName}\nRam Size:{self.ramsize}\nOs Version:{self.osversion}")

class Mobile(Device,Loader):
    def loadOS(self):
        print("Interface class method")

m=Mobile()
m.data()
m.loadOS()
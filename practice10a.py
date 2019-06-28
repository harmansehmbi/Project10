# is vs == Explore

""""
             Inheritance : IS-A Relationship | Generalization

             Maruti Suzuki Swift Desire IS-A swift

"""


class Shoe:
    def __init__(self, pid, name, price, brand, color, size):
        self.pid = pid
        self.name = name
        self.price = price
        self.brand = brand
        self.color = color
        self.size = size
    def updateShoeDetails(self, pid, name, price, brand, color, size):
        self.pid = pid
        self.name = name
        self.price = price
        self.brand = brand
        self.color = color
        self.size = size
    def showShoeDetails(self):
        print("======Shoe Details=====")
        print(self.pid)
        print(self.name)
        print(self.price)
        print(self.brand)
        print(self.color)
        print(self.size)
        print("=======================")
class Mobile:
    def __init__(self, pid, name, price, brand, ram, memory):
        self.pid = pid
        self.name = name
        self.price = price
        self.brand = brand
        self.ram = ram
        self.memory = memory
    def updateMobileDetails(self, pid, name, price, brand, ram, memory):
        self.pid = pid
        self.name = name
        self.price = price
        self.brand = brand
        self.ram = ram
        self.memory = memory
    def showMobileDetails(self):
        print("======Mobile Details=====")
        print(self.pid)
        print(self.name)
        print(self.price)
        print(self.brand)
        print(self.ram)
        print(self.memory)
        print("=======================")
class LEDTv:
    def __init__(self, pid, name, price, brand, technology, screenSize):
        self.pid = pid
        self.name = name
        self.price = price
        self.brand = brand
        self.technology = technology
        self.screenSize = screenSize
    def updateLEDTvDetails(self, pid, name, price, brand, technology, screenSize):
        self.pid = pid
        self.name = name
        self.price = price
        self.brand = brand
        self.technology = technology
        self.screenSize = screenSize
    def showLEDTvDetails(self):
        print("======LEDTv Details=====")
        print(self.pid)
        print(self.name)
        print(self.price)
        print(self.brand)
        print(self.technology)
        print(self.screenSize)
        print("=======================")
sRef = Shoe(101, "AlphaBounce", 8000, "Adidas", "Black", 9)
mRef = Mobile(201, "iPhoneX", 60000, "Apple", 4, 128)
lRef = LEDTv(301, "Samsung Curved LED", 80000, "Samsung", "OLED", 50)
sRef.showShoeDetails()
print()
mRef.showMobileDetails()
print()
lRef.showLEDTvDetails()

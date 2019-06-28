class Product:

    def __init__(self, pid, name, price, brand):
        self.pid = pid
        self.name = name
        self.price = price
        self.brand = brand


    def updateProductDetails(self, pid, name, price, brand):
        self.pid = pid
        self.name = name
        self.price = price
        self.brand = brand

    def showProductDetails(self):
        print("======Product Details=====")
        print(self.pid)
        print(self.name)
        print(self.price)
        print(self.brand)
        print("=======================")

class Shoe(Product): #IS-A Relation | Shoe IS-A Product | Inheritance

    def __init__(self, color, size):
        self.color = color
        self.size = size

    def updateShoeDetails(self, pid, name):
        self.color = color
        self.size = size

    def showShoeDetails(self):
        print("======Shoe Details=====")
        print(self.color)
        print(self.size)
        print("=======================")

class Mobile(Product):

    def __init__(self, pid, name, price, brand, ram, memory):
        Product.__init__(self, pid, name, price, brand)
        self.ram = ram
        self.memory = memory

    def updateMobileDetails(self, pid, name, price, brand, ram, memory):
        Product.updateProductDetails(self, pid, name, price, brand)
        self.ram = ram
        self.memory = memory

    # Overriding
    def showProductDetails(self):
        Product.showProductDetails(self)
        print("======Mobile Details=====")
        print(self.ram)
        print(self.memory)
        print("=======================")

class LEDTv(Product):

    def __init__(self,technology, screenSize):
        self.technology = technology
        self.screenSize = screenSize

    def updateLEDTvDetails(self, technology, screenSize):
        self.technology = technology
        self.screenSize = screenSize

    def showLEDTvDetails(self):
        print("======LEDTv Details=====")
        print(self.technology)
        print(self.screenSize)
        print("=======================")

mRef = Mobile(201, "iPhoneX", 60000, "Apple", 4, 128)
mRef.showProductDetails()


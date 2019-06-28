# Class and Object Relationship


class CA:
    num = 101

    def __init__(self):
        self.a = 102

    def show(self):
        print("num is: ", self.num)

        print("num is: ", CA.num)

    # Property of class can be accessed by class Vl


cRef = CA()

cRef.show()

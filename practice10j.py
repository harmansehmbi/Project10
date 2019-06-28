class CA:
    num = 101

    def __init__(self):
        self.a = 102

    def show(self):
        print("num is: ", self.num)
        # we can also use
        print("num is: ", CA.num)      # class name
        print("num is: ", ca.num)

ca = CA()

ca.show()

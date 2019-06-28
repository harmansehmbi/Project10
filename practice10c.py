# Inheritance

class Parent:

    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        print(">> Parent Constructor Executed")

    def showDetails(self):
        print(">>Hello", self.fname, self.lname)

class Child(Parent): # Relationship --> IS-A
    pass

print(Parent.__dict__)
print(Child.__dict__)

ch = Child("John", "Watson")



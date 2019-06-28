# Inheritance

class Parent:

    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        print(">> Parent Constructor Executed")

    def showDetails(self):
        print(">>Hello", self.fname, self.lname)

class Child(Parent): # Relationship --> IS-A

    def __init__(self, vehicle, salary):
        self.vehicle = vehicle
        self.salary = salary
        print(">> Child Constructor Executed ")

print("Parent Class Dictonary: ",Parent.__dict__)
print("Child Class Dictonary: ",Child.__dict__)

ch = Child("John", "Watson")
ch.fname = "George"
ch.lname = "Watson"
print(ch.__dict__)
ch.showDetails()


# Wrong way


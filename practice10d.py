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

print("Parent Class Dictonary: ",Parent.__dict__)
print("Child Class Dictonary: ",Child.__dict__)

ch = Child("John", "Watson")
print(ch.__dict__)
ch.showDetails()

# Rule 1. Whatsoever is in Parent class is accessible to child known as IS-A Relation
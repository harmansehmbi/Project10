# Inheritance

class Parent:

    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        print(">> Parent Constructor Executed")

    def showDetails(self):
        print(">>Hello", self.fname, self.lname)


class Child(Parent):  # Relationship --> IS-A

    def __init__(self, fname, lname, vehicle, salary):
        Parent.__init__(self, fname, lname)  # Customization
        self.vehicle = vehicle
        self.salary = salary
        print(">> Child Constructor Executed ")

    # Overriding
    def showDetails(self):  # can have same name as that of parent
        Parent.showDetails(self)
        print("Hello, ", self.vehicle, self.salary)


print("Parent Class Dictonary: ", Parent.__dict__)
print("Child Class Dictonary: ", Child.__dict__)

ch = Child("John", "Watson", 2, 30000)

print(ch.__dict__)
ch.showDetails()           # Child.showDetails()


Parent.showDetails(ch)   # this will work

# Rule 2. In child to have customisations, we shall access Parent's Properties
# Funda: If same function with the same name is also available

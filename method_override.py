# creating adult class with 4 attributes
class Adult:
    def __init__(self, name, age, eye_colour, hair_colour):
        self.name = name
        self.age = age
        self.eye_colour = eye_colour
        self.hair_colour = hair_colour

    # method if the driver is old enough to drive
    def can_drive(self):
        print(self.name, " is old enough to drive!")


# creating subclass (Child)
class Child(Adult):
    # method if driver is underaged
    def can_drive(self):
        print(self.name, " is too young to drive!")


# asking for the driver's details
name = input("Please insert a name here ")
age = int(input("Please add the driver's age: "))
eye_colour = input("Please tell the driver's eye colour")
hair_colour = input("Please tell the driver's hair colour")

# conditional statement to decide if the driver will be #
# underaged(instance of Child class) or Adult(instance of Adult class).
if age < 18:
    person = (Child(name, age, eye_colour, hair_colour))
else:
    person = (Adult(name, age, eye_colour, hair_colour))

# calling can_drive method
person.can_drive()

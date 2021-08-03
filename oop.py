# oop allows programmers to create their own objects that have methods and attributes and oop allows us to create code that is repeatable and organized.
# syntax:
class NameOfClass():

    def __init__(self, para1, para2):
        self.param1 = para1
        self.para2 = para2

    def some_method(self):
        #perform some action
        print(self.para1)

# OOP- class object attributes and methods


class Dog():
#constructor
# Attributes
# we take in the argument
# Assign it using self.attribute_name
    def __init__(self, mybreed):
        self.breed = mybreed
my_dog = Dog(mybreed = 'Lab')
# print(type(my_dog))
print(my_dog.breed)

# example 2
class cow():
    def __init__(self, breed, name, spots):
        self.breed = breed
        self.name = name
        # lets say spots is boolean(true/false)
        self.spots = spots
my_cow = cow(breed = 'jersey_Gai', name = 'Kali_Gai', spots = False )
print(my_cow.breed)
print(my_cow.name)
print(my_cow.spots)


# now class object attributes and methods as below:
# method is a function inside a class thats the difference between function n method

class buffalo():
    species = 'mammel'
    # mammel is the class attributes
    def __init__(self, breed, name):
        self.breed = breed
        self.name = name
    def bark(self):
        # bark is a method
        print(f"BWOO! my name is {self.name}")
my_buffalo = buffalo('Bhaisi', 'kale_Bhaisi')
print(my_buffalo.species)
# see attributes species never have ()
print(my_buffalo.breed)
print(my_buffalo.name)
# so lets see how to call method but method have()
print(my_buffalo.bark())

# example 3
# lets pass some parameter on method

class buffalo():
    species = 'mammel'
    # mammel is the class attributes
    def __init__(self, breed, name):
        self.breed = breed
        self.name = name
    def bark(self, number):
        # bark is a method
        # no need to call here for the number like self.number because we have to pass parameter later on when we call that function
        print(f"BWOO! my name is {self.name} and the Number is{number}")
my_buffalo = buffalo('Bhaisi', 'kale_Bhaisi')
print(my_buffalo.species)
# see attributes species never have ()
print(my_buffalo.breed)
print(my_buffalo.name)
# so lets see how to call method but method have()
print(my_buffalo.bark(10))


# example 4

class Circle():
    pi = 3.14
    # class object attribute
    def __init__(self, radius = 3):
        self.radius = radius
        self.area = radius * radius * self.pi
#         method
    def get_circumfrence(self):
        return self.radius * self.pi * 2
#     or return self.radius * Circle.pi * 2
my_circle = Circle()
# in above we didnot pass any value because radius have a defult value but if we pass its gonna be overridden
print(my_circle.pi)
print(my_circle.radius)
print(my_circle.get_circumfrence())
print(my_circle.area)















# inheritance and polymorphism

class Animal():
    def __init__(self):
        print("anilmal created")


    def who_am_i(self):
        print("i am an animal")


    def eat(self):
        print("i am eating")


class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print ("Dog created")

    def eat(self):
        return "i am a dog and eating"
    # function overridding here

    def bark(self):
        return "WOOF"

mydog = Dog()
print(mydog)
print(mydog.bark())
print(mydog.eat())


# polymorphism

class Dog():
    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + " says woof"

class Cat():
    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + " says meow"
#     in above case both Dog and Cat have same function name called speak

niko = Dog("niko")
biralo = Cat("biralo")
print(niko.speak())
print(biralo.speak())


for pet in [niko, biralo]:
    print(type(pet))
    print(pet.speak())




# Abstract class

class Animal():
    def __init__(self, name):
        self.name = name

    def speak(self):
        








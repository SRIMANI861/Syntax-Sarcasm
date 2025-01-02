"""Inheritance is a concept of deriving the child class from parent class
-> Parent class is also called as base class or super class 
-> child class is also called as or subclass or derived class

We have different types in inheritance:
1. Single inheritance
2. Multiple inheritance
3. Multilevel inheritance
4. Hierarchical inheritance
5. Hybrid inheritance

"""

"""
1. Single Inheritance: a child class inherit properties from single parent class.
"""
class Animal:
    def sound(self):
        print('animal makes a sound')
class Dog(Animal):
    def bark(self):
        print('dogs bark')
dog = Dog()
dog.sound()
dog.bark()

"""
2. Multiple Inheritance: a child class is inherited from multiple parents
"""
class Mother:
    def trait(self):
        print("Mother: love and caring")
class Father:
    def traits2(self):
        print("Father: responsibility and strong")
class Child(Mother, Father):
    def traits(self):
        super().trait() #the first parent class will be called
    #Calling specific parent class methods
        # Mother.traits(self)
        # Father.traits(self)
        print("child inherits both parents")
child = Child()
child.traits()
child.trait()
child.traits2()

"""
3. Multilevel inheritance: A child class is derived from a parent class and parent is derived from grand parent class.
"""
class Animal: #parent class
    def sound(self):
        print('animal makes sound')
class Dog(Animal): #intermediate child class
    def bark(self):
        print('dogs bark')
class Puppy(Dog): #child class
    def play(self):
        print('puppies love to play')
puppy = Puppy()
puppy.sound()
puppy.bark()
puppy.play()

"""
4.Hierarchical Inheritance: Multiple child classes inherit from a single parent class
"""
class Animal:
    def sound(self):
        print("animal make a sound")
class Dog(Animal):
    def barks(self):
        print('Dog barks')
class Cat(Animal):
    def meow(self):
        print('Cat meows')
dog = Dog()
dog.sound()
dog.barks()
cat = Cat()
cat.sound()
cat.meow()

"""
5. Hybrid Inheritance: combine 2 or more types of inheritance
"""
class Animal:
    def sound(self):
        print('animal makes a sound')
class Dog(Animal):
    def barks(self):
        print('Dog barks')
class Pet:
    def friendly(self):
        print('pets are friendly')
class Puppy(Dog,Pet): #multiple inheritance as puppy is derived from both dog and pet and it is also #multilevel inheritance as Dog is derived from Animal and puppy is derived from Dog
    def plays(self):
        print('puppy plays well')
puppy = Puppy()
puppy.sound()
puppy.barks()
puppy.friendly()
puppy.plays()


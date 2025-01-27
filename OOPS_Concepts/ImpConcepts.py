class Person:
    def __init__(self,name,age): #init is a constructor used to define object attributes, we have initialized the values using init constructor
        self.name = name #self.name is an instance and we are assigning the value name to the instance
        self.age = age
        print(f"Person object created: {self.name},{self.age}")
p1 = Person("tom",25) #for creating these values, we are using constructors to initialize the values(__init__(self,name,age)) => these are the variables initialized with the __init__ constructor
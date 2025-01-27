class Car:
    
    """
    self is a special keyword used inside a class to refer to the current instance of a class. 
    Why we use self?
        - It allows us to access variables and methods that belong to specific object created from the class
        --It helps to differentiate from instance variables and local variables defined in a method

        --It helps to make methods and variables specific to object, rather than shared globally
        -- We can use any name in place of self, it is NOT a reserved keyword
    """
    def __init__(self,brand,model): 
        self.brand = brand
        self.model = model
    def display_info(self): #no need to give brand and model parameters again
        print(f"car brand is {self.brand} and model is {self.model}")
car1 = Car('Rolls Royce', 'Corolla')
car2 = Car('Benz', 'civic')
car3 = Car('Toyota','something')
car1.display_info()
car2.display_info()
car3.display_info()
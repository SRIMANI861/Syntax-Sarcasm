class Car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
    def display_info(self):
        print(f"car brand is {self.brand} and model is {self.model}")
car1 = Car('Rolls Royce', 'Corolla')
car2 = Car('Benz', 'civic')
car3 = Car('Toyota','something')
car1.display_info()
car2.display_info()
car3.display_info()
# Define the Car class
class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    # Method to display car details
    def display_info(self):
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")


# Create an object of Car
my_car = Car("Toyota", "Corolla", 2022)

# Call the method
my_car.display_info()

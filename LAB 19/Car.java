// Define the Car class
public class Car {
    // Attributes
    String brand;
    String model;
    int year;

    // Constructor
    public Car(String brand, String model, int year) {
        this.brand = brand;
        this.model = model;
        this.year = year;
    }

    // Method to display car details
    public void displayDetails() {
        System.out.println("Brand: " + brand);
        System.out.println("Model: " + model);
        System.out.println("Year: " + year);
    }
    public static void main(String[] args) {
        // Create an object
        Car myCar = new Car("Toyota", "Corolla", 2022);

        // Call the method
        myCar.displayDetails();
    }
}

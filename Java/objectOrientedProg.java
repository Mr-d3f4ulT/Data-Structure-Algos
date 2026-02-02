class Car {
  String model;
  String color;
  int year;
  int price;

  Car() {
    model = "BMW M4 Competition";
    color = "Black";
    year = 2025;
    price = 108800;
  }
  Car(String model, String color, int year, int price) {
    this.model = model;
    this.color = color;
    this.year = year;
    this.price = price;
  }

  void drive() {
    System.out.println("You are driving a " + color + " " + year + " " + model + " priced at $" + price);
  }
  void stop() {
    System.out.println("The " + model + " has stopped.");
  }
}
public class objectOrientedProg {
  public static void main(String[] args) {
    // Object-Oriented Programming (OOP) = programming paradigm based on the concept of "objects", which can contain data and code.
    // Four Pillars of OOP: Encapsulation, Abstraction, Inheritance, Polymorphism

    // Encapsulation = the bundling of data (attributes) and methods (functions) that operate on the data into a single unit or class.
    // It restricts direct access to some of an object's components, which can prevent the accidental modification of data.
    // Access Modifiers: public, private, protected, default

    // Abstraction = the concept of hiding the complex implementation details and showing only the essential features of the object.
    // It helps in reducing programming complexity and effort.

    // Inheritance = a mechanism where a new class inherits properties and behavior (methods) from an existing class.
    // It promotes code reusability and establishes a relationship between classes.

    // Polymorphism = the ability of a variable, function, or object to take on multiple forms.
    // It allows methods to do different things based on the object it is acting upon, even though they share the same name.

    System.out.println("Object-Oriented Programming Concepts in Java");
    Car obj;
    obj = new Car();
    //obj = new Car("Porsche 911 GT3 RS", "Matte Black", 2026, 250000);
    obj.drive();
    obj.stop();
  }
}

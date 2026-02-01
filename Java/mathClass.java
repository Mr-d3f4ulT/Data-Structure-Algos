import java.util.*;
public class mathClass {
  public static void main(String[] args) {
    int x = -10;
    int y = 3;
    int z = 16;
    System.out.println("Value of x is : " + x + ", y is : " + y + ", z is : " + z);
    System.out.println("Max number is " + Math.max(y, z)); // Gives maximum value between y and z
    System.out.println("Min number is " + Math.min(y, z)); // Gives minimum value between y and z
    System.out.println("Absolute value of x is " + Math.abs(x)); // Gives absolute value of x
    System.out.println("Square root of z is " + Math.sqrt(z)); // Gives square root of z
    System.out.println("Rounded value of 4.6 is " + Math.round(4.6)); // Rounds the value to nearest integer
    System.out.println("Ceiling value of 4.2 is " + Math.ceil(4.2)); // Rounds the value up to nearest integer
    System.out.println("Floor value of 4.8 is " + Math.floor(4.8)); // Rounds the value down to nearest integer
    System.out.println("y raised to the power of 2 is " + Math.pow(y, 2)); // Gives y raised to the power of 2
    System.out.println("Random number between 0.0 and 1.0 is " + Math.random()); // Gives a random number between 0.0 and 1.0
    System.out.println("Random number between 0 and 100 is " + (int)(Math.random() * 101)); // Gives a random number between 0 and 100
  }
}

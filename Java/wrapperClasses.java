public class wrapperClasses {
  public static void main(String[] args) {
    //Wrapper Class = provides a way to use primitive data types (int, char, boolean, etc..) as reference data types (objects).
    // can be used when working with collections (ex. ArrayList, HashMap, etc..)

    //Primitive Data Types   // Wrapper Classes
    // byte                  Byte
    // short                 Short
    // int                   Integer
    // long                  Long
    // float                 Float
    // double                Double
    // char                  Character
    // boolean               Boolean

    // Autoboxing = the automatic conversion that the Java compiler makes between the primitive data types and their corresponding object wrapper classes.
    // Unboxing = the reverse process of converting an object of a wrapper class to its corresponding primitive data type.

    //Autoboxing Example
    Boolean boolObj = true; 
    Character charObj = 'A'; 
    Integer intObj = 100; 
    Double doubleObj = 99.99; 
    Float floatObj = 65.55f;

    System.out.println(boolObj.booleanValue()); // Unboxing
    System.out.println(charObj.charValue());   // Unboxing
    System.out.println(intObj.intValue());     // Unboxing
    System.out.println(doubleObj.doubleValue()); // Unboxing
    System.out.println(floatObj.floatValue()); // Unboxing
  }
}

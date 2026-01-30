class strings {
  public static void main(String[] args) {
    String message = "New String Example";
    System.out.println("Original Message : " + message);
    
    System.out.println(message.endsWith("!!")); // false

    System.out.println(message.length()); // 18
    System.out.println(message.replace("New String Example", "Lana Rhoades"));  // Lana Rhoades
    System.out.println(message.toLowerCase());  
    System.out.println(message.toUpperCase());
    System.out.println(message.compareTo("Another String"));
    System.out.println(message.equals("New String Example")); // true
  }
}

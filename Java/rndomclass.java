import java.util.Random;
public class rndomclass {
  public static void main(String[] args) {
    Random rand = new Random();

    // Generate a random integer
    int randomInt = rand.nextInt(100); // Random integer between 0 and 99
    System.out.println("Random Integer: " + randomInt);

    // Generate a random double
    double randomDouble = rand.nextDouble(); // Random double between 0.0 and 1.0
    System.out.println("Random Double: " + randomDouble);

    // Generate a random float
    float randomFloat = rand.nextFloat();
    System.out.println("Random Float: " + randomFloat);

    // Generate a random boolean
    boolean randomBoolean = rand.nextBoolean();
    System.out.println("Random Boolean: " + randomBoolean);
  }
}

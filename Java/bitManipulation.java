class bitManipulationProblems {
  public String IntegertoBinary(int n) { //TC : O(log n), where n is the input integer. SC : O(log n) for storing the binary representation in the StringBuilder.
    StringBuilder binary = new StringBuilder();
    while (n > 0) {
      int bit = n % 2;
      binary.append(bit);
      n /= 2;
    }
    return binary.reverse().toString();
  }
}
public class bitManipulation {
  public static void main(String[] args) {
    
  }
}

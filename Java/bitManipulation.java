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
  public int BianryToDecimal(String binary) { //TC : O(n), where n is the length of the binary string. SC : O(1) for storing the decimal value.
    int len = binary.length();  
    int decimalValue = 0;
    for(int i = len - 1; i >= 0; i--) {
      int bit = binary.charAt(i) - '0'; // Convert character to integer (0 or 1)
      decimalValue = decimalValue + bit * (int)Math.pow(2, len - 1 - i);
    }
    return decimalValue;
  }
}
public class bitManipulation {
  public static void main(String[] args) {
    // bitManipulationProblems obj = new bitManipulationProblems();
    // int n = 10;
    // String binary = obj.IntegertoBinary(n);
    // System.out.println("Binary representation of " + n + " is: " + binary);
    
    // String binaryString = "1010";
    // int decimalValue = obj.BianryToDecimal(binaryString);
    // System.out.println("Decimal value of binary string " + binaryString + " is: " + decimalValue);

  }
}

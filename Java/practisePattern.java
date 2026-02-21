class pattern {
  void squareHollow(int n) {
    for(int i = 0; i < n; i++) {
      for(int j = 0; j < n; j++) {
        if(i == 0 || i == n - 1 || j == 0 || j == n - 1) {
          System.out.print("* ");
        } else {
          System.out.print("  ");
        }
      }
      System.out.println();
    }
  }
  void numberTraingular(int n) {
    for(int i = 1; i <= n; i++) {
      //Inner loop for printing spaces
      for(int j = 1; j <= n - i; j++) { 
        System.out.print(" ");
      }
      //Inner loop for printing numbers
      for(int k = 1; k <= i; k++) {
        System.out.print(i + " ");
      }
      System.out.println();
    }
  }
  void numberIncreasingPyramid(int n) {
    for(int i = 1; i <= n; i++) {
      for(int j = 1; j <= i; j++) {
        System.out.print(j + " ");
      }
      System.out.println();
    }
  }
  void numberIncreasingReversePyramid(int n) {
    for(int i = 1; i <= n; i++) {
      for(int j = 1; j <= n -i + 1; j++) {
        System.out.print(j + " ");
      }
      System.out.println();
    }
  } 
}
public class practisePattern {
  public static void main(String[] args) {
    pattern p = new pattern();
    //p.squareHollow(5);
    //p.numberTraingular(5);
    //p.numberIncreasingPyramid(5);
    p.numberIncreasingReversePyramid(5);
  }
}

class pattern {
  int i, j, k;
  void squareHollow(int n) {
    for(i = 0; i < n; i++) {
      for(j = 0; j < n; j++) {
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
    for(i = 1; i <= n; i++) {
      //Inner loop for printing spaces
      for(j = 1; j <= n - i; j++) { 
        System.out.print(" ");
      }
      //Inner loop for printing numbers
      for(k = 1; k <= i; k++) {
        System.out.print(i + " ");
      }
      System.out.println();
    }
  }
  void numberIncreasingPyramid(int n) {
    for(i = 1; i <= n; i++) {
      for(j = 1; j <= i; j++) {
        System.out.print(j + " ");
      }
      System.out.println();
    }
  }
  void numberIncreasingReversePyramid(int n) {
    for (i = n; i >= 1; i--) {
      for (j = 1; j <= i; j++) {
        System.out.print(j + " ");
      }
      System.out.println();
    }
  } 
  void numberChangingPyramid(int n) {
    int num = 1;
    for(i = 1; i <= n; i++) {
      for(j = 1; j <= i; j++) {
        System.out.print(num + " ");
        num++;
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
    //p.numberIncreasingReversePyramid(5);
    p.numberChangingPyramid(5); 
  }
}

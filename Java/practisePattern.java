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
  void zeroOneTriangle(int n) {
    for(i = 1; i <= n; i++) {
      for(j = 1; j <= i; j++) {
        if((i + j) % 2 == 0) {
          System.out.print("1 ");
        } else {
          System.out.print("0 ");
        }
      }
      System.out.println();
    }
  }
  void palindromeTriangle(int n) {
    for(i = 1; i <=n; i++) {
      //Inner loop for printing spaces
      for(j = 1; j <= 2*(n - i); j++) {
        System.out.print(" ");
      }
      //Inner loop for printing decreasing numbers till 1
      for(k = i; k >= 1; k--) {
        System.out.print(k + " ");
      }
      //Inner loop for printing increasing numbers starting from 2 cause we alredy printed 1 in the previous loop
      for(j = 2; j <= i; j++) {
        System.out.print(j + " ");
      }
      System.out.println();
    }
  }
  void rhombus(int n) {
    for(i = 1; i <= n; i++) {
      //Inner loop for spaces
      for(j = 1; j <= n - i; j++) {
        System.out.print(" ");
      }
      //Inner loop for printing stars
      for(k = 1; k <= n; k++) {
        System.out.print("* ");
      }
      System.out.println();
    }
  }
  void diamondPattern(int n) {
    //Outer loop for upper half of the diamond
    for(i = 1; i <= n; i++) {
      //Inner loop for spaces for upper half of the diamond
      for(j = 1; j <= n - i; j++) {
        System.out.print(" ");
      }
      //Inner loop for printing stars for upper half of the diamond
      for(k = 1; k <= 2 * i - 1; k++) {
        System.out.print("*");
      }
      System.out.println(); 
    }

    //Outer loop for lower half of the diamond
    for(i = n - 1; i >= 1; i--) {
      //Inner loop for spaces
      for(j = 1; j <= n - i; j++) {
        System.out.print(" ");
      }
      //Inner loop for printing stars
      for(k = 1; k <= 2*i - 1; k++) {
        System.out.print("*");
      }
      System.out.println(); 
    }
  }
  void butterflyPattern(int n) {
    //Outer loop for upper half of the butterfly
    for(i = 1; i <= n; i++) {
      //Inner loop for printing stars for left wing of the butterfly
      for(j = 1; j <= i; j++) {
        System.out.print("*");
      }
      //Inner loop for spaces between the wings of the butterfly
      for(k = 1; k <= 2 * (n - i); k++) {
        System.out.print(" ");
      }
      //Inner loop for printing stars for right wing of the butterfly
      for(j = 1; j <= i; j++) {
        System.out.print("*");
      }
      System.out.println();
    }

    //Outer loop for the lower half of the butterfly
    for(i = n - 1; i >= 1; i--) {
      //Inner loop for printing stars for left wing of the butterfly
      for(j = 1; j <= i; j++) {
        System.out.print("*");
      }
      //Inner loop for spaces between the wings of the butterfly
      for(k = 1; k <= 2 * (n - i); k++) {
        System.out.print(" ");
      }
      //Inner loop for printing stars for right wing of the butterfly
      for(j = 1; j <= i; j++) {
        System.out.print("*");
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
    //p.numberChangingPyramid(5); 
    //p.zeroOneTriangle(5);
    //p.palindromeTriangle(5);
    //p.rhombus(5);
    //p.diamondPattern(5);
    p.butterflyPattern(5);
  }
}

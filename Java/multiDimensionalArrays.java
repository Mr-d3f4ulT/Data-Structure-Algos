import java.util.Arrays;
public class multiDimensionalArrays {
  public static void main(String[] args) {
    int[][] matrix = {
      {1, 2, 3},
      {4, 5, 6},
      {7, 8, 9}
    };
    System.out.println("Original Matrix:");
    for (int i = 0; i < matrix.length; i++) {
      for (int j = 0; j < matrix[i].length; j++) {
        System.out.print(matrix[i][j] + " ");
      }
      System.out.println();
    }

    System.out.println("Number of Rows: " + matrix.length);
    System.out.println("Number of Columns in first row: " + matrix[0].length);
    System.out.println("Matrix : " + Arrays.deepToString(matrix));
  }
}

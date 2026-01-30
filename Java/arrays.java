import java.util.Arrays;
public class arrays {
  public static void main(String[] args) {
    int[] nums = {10, 20, 30, 40, 50};
    System.out.print("Original Array: | ");
    for (int i : nums) {
      System.out.print(i + " | ");
    }

    System.out.println();
    System.out.println("Array Length: " + nums.length);
    System.out.println("Array toString(): " + Arrays.toString(nums));
  }
}

import java.util.Arrays;
public class arrays {
  public static void main(String[] args) {
    int[] nums = {10, 30, 20, 40, 50};
    System.out.print("Original Array: | ");
    for (int i : nums) {
      System.out.print(i + " | ");
    }

    System.out.println();
    System.out.println("Array Length: " + nums.length);  // Length of the array
    System.out.println("Array to String : " + Arrays.toString(nums)); // Convert array to string
    Arrays.sort(nums); // Sort the array
    System.out.println("Sorted Array: " + Arrays.toString(nums));
    
    int[] newArr = Arrays.copyOf(nums, 3); // Copy first 3 elements to new array
    System.out.println("Copied Array: " + Arrays.toString(newArr));

    Arrays.fill(newArr, 100); // Fill the array with 100
    System.out.println("Filled Array: " + Arrays.toString(newArr));

    System.out.println(Arrays.equals(nums, newArr)); // Compare two arrays

    
  }
}

class problems {
    void oddEven(int n) {
        if((n & 1) == 1) System.out.println("Odd");
        else System.out.println("Even");
    }
    void findElementRepeatingOnce(int[] arr) {
        //Find the element repeating once in an array of elements
        int repeatOnce = 0;
        for(int i = 0; i < arr.length; i++) {
            repeatOnce = repeatOnce ^ arr[i];
        }
        System.out.println(repeatOnce);
    }
}
public class bitManipulationProblems {
    public static void main(String[] args) {
        problems p = new problems();
        int n = 27;
        int[] arr = {1,2,5,6,2,1,5};
        p.oddEven(n);
        p.findElementRepeatingOnce(arr);
    }
}

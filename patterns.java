

public class patterns {
    
    public static void pattern2(int n) {
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j < i; j++) {
                System.out.print("* "); // For Ans2
                System.out.print(j + " "); // For Ans3
            }
            System.out.println();
        }
    }
    
    public static void pattern3(int n) {
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j < i; j++) {
                System.out.print(j + " ");
            }
            System.out.println();
        }
    }
    
    public static void pattern7(int n) {
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= n - i - 1; j++) {
                System.out.print("  ");
            }
            for (int k = 1; k <= (2 * i + 1); k++) {
                System.out.print("* ");
            }
            for (int j = 1; j <= n - i - 1; j++) {
                System.out.print("  ");
            }
            System.out.println();
        }
    }
    
    public static void pattern8(int n) {
        int gap = 0, stars = 2 * n - 1;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < gap; j++) {
                System.out.print(" ");
            }
            for (int j = gap; j < gap + stars; j++) {
                System.out.print("*");
            }
            System.out.println();
            gap++;
            stars -= 2;
        }
    }
    
    public static void pattern10(int n) {
        for (int i = 1; i <= 2 * n - 1; i++) {
            int stars = i;
            if (i > n) stars = 2 * n - i;
            for (int j = 1; j <= stars; j++) {
                System.out.print("*");
            }
            System.out.println();
        }
    }
    
    public static void pattern11(int n) {
        int num = 1;
        for (int i = 0; i < n; i++) {
            for (int j = 1; j <= num; j++) {
                System.out.print(((i + j) & 1) + " ");
            }
            System.out.println();
            num++;
        }
    }
    
    public static void pattern12(int n) {
        int num = 1, gap = (n - 1) * 2;
        for (int i = 0; i < n; i++) {
            int currentNumber = 1;
            for (int j = 1; j <= num; j++) {
                System.out.print(currentNumber + " ");
                currentNumber++;
            }
            for (int j = 1; j <= gap; j++) {
                System.out.print("  ");
            }
            currentNumber--;
            for (int j = 1; j <= num; j++) {
                System.out.print(currentNumber + " ");
                currentNumber--;
            }
            System.out.println();
            num++;
            gap -= 2;
        }
    }
    
    public static void pattern17(int n) {
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n - i - 1; j++) {
                System.out.print(" ");
            }
            char alpha = 'A';
            int breakpoint = (2 * i + 1) / 2;
            for (int k = 1; k <= 2 * i + 1; k++) {
                System.out.print(alpha + " ");
                if (k <= breakpoint) alpha++;
                else alpha--;
            }
            System.out.println();
        }
    }
    
    public static void pattern18(int n) {
        for (int row = 0; row < n; row++) {
            for (int col = 0; col <= row; col++) {
                System.out.print((char) (n - col - 1 + 'A') + " ");
            }
            System.out.println();
        }
    }
    
    public static void pattern19(int n) {
        int iniS = 0;
        // Upper Half
        for (int i = 0; i < n; i++) {
            for (int k = 0; k < n - i; k++) {
                System.out.print("*");
            }
            for (int j = 0; j < iniS; j++) {
                System.out.print(" ");
            }
            for (int k = 0; k < n - i; k++) {
                System.out.print("*");
            }
            iniS += 2;
            System.out.println();
        }
        // Lower Half
        iniS = 2 * n - 2;
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= i; j++) {
                System.out.print("*");
            }
            for (int j = 0; j < iniS; j++) {
                System.out.print(" ");
            }
            for (int j = 1; j <= i; j++) {
                System.out.print("*");
            }
            iniS -= 2;
            System.out.println();
        }
    }
    
    public static void main(String[] args) {
        int n = 3; //int N = 5;
        System.out.println("Patterns Problem of Striver's A2Z DSA Course/Sheet");
        pattern19(n);
    }
}

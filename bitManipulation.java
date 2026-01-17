
class operatorsJava {
    public void arithmeticOperators() {
        int num1 = 8, num2 = 4;

        System.out.println("Arithmetic Operators : ");
        System.out.println("Addition( + ) : " + (num1 + num2));
        System.out.println("Subtraction( - ) : " + (num1 - num2));
        System.out.println("Multiplication( * ) : " + (num1 * num2));
        System.out.println("Division( / ) : " + (num1 / num2));
        System.out.println("Modulus( % ) : " + (num1 % num2));
    }
    public void unaryOperators() {
        //Java unary operators are the types that need only one operand to perform any operation like increment, decrement, negation, etc. It consists of various arithmetic, logical and other operators that operate on a single operand.
        int num = 10;
        // Unary plus
        int result = +num;
        System.out.println("The value of result after unary plus is: " + result);
        // Unary minus
        result = -num;
        System.out.println("The value of result after unary minus is: " + result);
        // Pre-increment
        result = ++num;
        System.out.println("The value of result after pre-increment is: " + result);
        // Post-increment
        result = num++;
        System.out.println("The value of result after post-increment is: " + result);
        // Pre-decrement
        result = --num;
        System.out.println("The value of result after pre-decrement is: " + result);
        // Post-decrement
        result = num--;
        System.out.println("The value of result after post-decrement is: " + result);

    }
    public void assingmentOperators() {
        int num1 = 10, num2;
        System.out.println("Assingment Operators : ");
        System.out.println("1. Equal(=) : assign value on right to variable on left -> " + (num2 = num1));
        System.out.println("2. += -> " + (num2 += num1));
        System.out.println("3. -= -> " + (num2 -= num1));
        System.out.println("4. *= -> " + (num2 *= num1));
        System.out.println("5. /= -> " + (num2 /= num1));
        System.out.println("6. %= -> " + (num2 %= num1));
    }
    public void relationalOperators() {
        int num1 =1;
        int num2 = 2;
        System.out.println("Relational Operators : ");
        System.out.println("num1 > num2 is " + (num1 > num2));
        System.out.println("num1 < num2 is " + (num1 < num2));
        System.out.println("num1 >= num2 is " + (num1 >= num2));
        System.out.println("num1 <= num2 is " + (num1 <= num2));
        System.out.println("num1 == num2 is " + (num1 == num2));
        System.out.println("num1 != num2 is " + (num1 != num2));
    }
    public void logicalOperators() {
        boolean a = true;
        boolean b = false;
        System.out.println("Logical Operatos : ");
        System.out.println("a: " + a);
        System.out.println("b: " + b);
        System.out.println("a && b: " + (a && b));
        System.out.println("a || b: " + (a || b));
        System.out.println("!a: " + !a);
        System.out.println("!b: " + !b);
    }
    public void ternaryOperators() {
        int n1 = 5, n2 = 10, res;
        System.out.println("First num: " + n1);
        System.out.println("Second num: " + n2);
        res = (n1 > n2) ? (n1 + n2) : (n1 - n2);
        System.out.println("Result = " + res);
    }
    public void bitwiseOperator() {
        int a = 5;
        int b = 7;
        System.out.println("Bitwise Operator : ");
        System.out.println("1. Bitwise AND : ");
        // 0101 & 0111=0101 = 5
        System.out.println("a&b = " + (a & b));

        System.out.println("2. Bitwise OR : ");
        // 0101 | 0111=0111 = 7
        System.out.println("a|b = " + (a | b));

        System.out.println("3. Bitwise XOR : ");
        // 0101 ^ 0111=0010 = 2
        System.out.println("a^b = " + (a ^ b));

        System.out.println("4. Bitwise COMPLIMENT : ");
        // ~00000000 00000000 00000000 00000101=11111111 11111111 11111111 11111010
        // will give 2's complement (32 bit) of 5 = -6
        System.out.println("~a = " + ~a);
        /*
            * Bitwise operators can be combined with assingment operators to provide shorthand representation
                ex- a &= a;
        */

    }
    public void bitShiftOperator() {
        /*
            * Shift operators are used to shift the bits of a number left or right, thereby multiplying or dividing the number by two, respectively. They can be used when we have to multiply or divide a number by two.
            * Types : Shift Operators are further divided into 3 types.
                * Signed Left shift operator (<<) : The left shift operator moves all bits by a given number of bits to the left.
                * Signed Right shift operator (>>) : The right shift operator moves all bits by a given number of bits to the right.
                * Unsighned Right Shift operator(>>>) : It is the same as the signed right shift, but the vacant leftmost position is filled with 0 instead of the sign bit.
         */
        int num1 = 20;
        int num2 = -20;
        System.out.println("Bitwise Signed Left Shift: " + (num1 << 2));
        System.out.println("Bitwise Signed Right Shift: " + (num1 >> 2));
        System.out.println("Bitwise Unsigned Right Shift for positive number :  " + (num1 >>> 2));
        System.out.println("Bitwise Unsigned Right Shift for negative number : " + (num2 >>> 2));
    }
}
class bitOperations {
    // Function to get the bit at the ith position
    public boolean getBit(int num, int i)
    {
        // Return true if the ith bit is set. Otherwise, return false
        return ((num & (1 << i)) != 0);
    }
    // Function to set the ith bit of the given number num
    public int setBit(int num, int i)
    {
        // Sets the ith bit and return the updated value
        return num | (1 << i);
    }
    // Function to clear the ith bit of the given number num
    public int clearBit(int num, int i)
    {
        // Create the mask for the ith bit unset
        int mask = ~(1 << i);
        // Return the updated value
        return num & mask;
    }
}
public class bitManipulation {
    public static void main(String[] args) {
        operatorsJava oj = new operatorsJava();
        //oj.arithmeticOperators();
        //oj.unaryOperators();
        //oj.assingmentOperators();
        //oj.relationalOperators();
        //oj.logicalOperators();
        //oj.ternaryOperators();
        //oj.bitwiseOperator();
        oj.bitShiftOperator();
        bitOperations ob = new bitOperations();
        int N = 70;
        System.out.println("The bit at the 3rd position from LSB is: " + (ob.getBit(N, 3) ? '1' : '0'));
        System.out.println("The value of the given number " + "after setting the bit at " + "LSB is: " + ob.setBit(N, 0));
        System.out.println("The value of the given number " + "after clearing the bit at " + "LSB is: " + ob.clearBit(N, 0));
    }
}

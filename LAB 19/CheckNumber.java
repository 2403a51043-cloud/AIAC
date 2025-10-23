import java.util.Scanner;

public class CheckNumber {
    
    // Method to check if number is positive, negative, or zero
    public static void checkNumber(int num) {
        if (num > 0) {
            System.out.println("The number is positive");
        } else if (num < 0) {
            System.out.println("The number is negative");
        } else {
            System.out.println("The number is zero");
        }
    }public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter a number: ");
        int num1 = sc.nextInt();
        checkNumber(num1);  // call method

        System.out.print("Enter another number: ");
        int num2 = sc.nextInt();
        checkNumber(num2);  // call method

        System.out.print("Enter one more number: ");
        int num3 = sc.nextInt();
        checkNumber(num3);  // call method

        sc.close();
    }
}

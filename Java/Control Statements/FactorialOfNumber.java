import java.util.*;

class FactorialOfNumber {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        int factorial = 1;
        int n = sc.nextInt();
        if (n == 0) {
            System.out.println("1");
        } else if (n <= 0) {
            System.out.println("Error");
        } else {
            for (int i = 1; i <= n; i++) {
                factorial *= i;
            }
            System.out.println(factorial);
        }
        sc.close();

    }
}
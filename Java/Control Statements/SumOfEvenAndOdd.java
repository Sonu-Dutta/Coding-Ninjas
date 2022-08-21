import java.util.Scanner;

class SumOfEvenAndOdd {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        int num = sc.nextInt();
        int evenSum = 0;
        int oddSum = 0;
        int temp = num;
        while (temp > 0) {
            int remainder = temp % 10;
            temp = temp / 10;
            if (remainder % 2 == 0)
                evenSum += remainder;
            else
                oddSum += remainder;
        }
        System.out.println(evenSum + " " + oddSum);
        sc.close();
    }
}
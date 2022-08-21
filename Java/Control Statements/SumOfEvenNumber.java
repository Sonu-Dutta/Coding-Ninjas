import java.util.Scanner;

public class SumOfEvenNumber {

    public long evenSumTillN(int n) {
        long sum = 0;
        for (int i = 2; i <= n; i++) {
            if (i % 2 == 0) {
                sum = sum + i;
            }
        }
        return sum;

    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        SumOfEvenNumber sum = new SumOfEvenNumber();
        System.out.println(sum.evenSumTillN(n));
        sc.close();
    }

}
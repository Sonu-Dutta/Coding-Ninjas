import java.util.Scanner;

class CalculateSimpleInterest {

    public static void main(String args[]) {

        int p, t, si;
        float rate;
        Scanner sc = new Scanner(System.in);
        p = sc.nextInt();
        rate = sc.nextFloat();
        t = sc.nextInt();

        si = (int) (p * rate * t) / 100;
        System.out.println(si);
        sc.close();
    }
}
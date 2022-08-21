import java.util.Scanner;

public class LargestOf3Numbers {

    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        int val1 = sc.nextInt();
        int val2 = sc.nextInt();
        int val3 = sc.nextInt();
        if ((val1 > val2 && val1 > val3)) {
            System.out.println(val1);
        } else if ((val2 > val1 && val2 > val3)) {
            System.out.println(val2);
        } else {
            System.out.println(val3);
        }
        sc.close();
    }
}
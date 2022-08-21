
import java.util.*;

class FindPowerOfNumber {

    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        int x = sc.nextInt();
        int n = sc.nextInt();
        if (x == 0 && n == 0) {
            System.out.println("1");
        } else {
            int Power = (int) Math.pow(x, n);
            System.out.println(Power);

        }
        sc.close();
    }
}
import java.util.*;

class FahrenheitToCelsius {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        int S = sc.nextInt();
        int E = sc.nextInt();
        int W = sc.nextInt();
        for (int i = S; i < E; i += W) {
            System.out.println(i + "\t" + ((i - 32) * 5) / 9);
        }
        sc.close();
    }
}

public class NthFibonacciNumber {
    public static int fibonacciNumber(int n) {
        long mod = 1000000007;
        long a = 0;
        long b = 1;
        long c = 0;
        for (int i = 0; i < n; i++) {
            c = (a % mod + b % mod);
            a = b % mod;
            b = c % mod;
        }
        return (int) a;
    }
}
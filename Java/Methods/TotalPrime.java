import java.util.Scanner;

class CountPrime {
    boolean checkPrime(int n) {
        for (int i = 2; i <= n / 2; i++) {
            if (n % i == 0)
                return false;
        }
        return true;
    }

    int totalPrime(int s, int e) {
        int cnt = 0;
        for (int i = s; i <= e; i++) {
            if (checkPrime(i))
                cnt++;
        }
        return cnt;
    }
}

class TotalPrime {
    public static void main(String args[]) {

        CountPrime obj = new CountPrime();
        Scanner sc = new Scanner(System.in);
        int s = sc.nextInt();
        int e = sc.nextInt();
        System.out.println(obj.totalPrime(s, e));
        sc.close();
    }
}

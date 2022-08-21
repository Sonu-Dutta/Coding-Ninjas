import java.util.*;
// solution 1

// import javafx.util.Pair;
// public class Solution {
//    public static Pair < Integer, Integer > swap(Pair < Integer, Integer > swapValues) {
//       Pair<Integer,Integer>ans=new Pair(swapValues.getValue(),swapValues.getKey());
//       return ans;
//    }
// }

// solution 2
class SwapTwoNumbers {
    static void swap(int m, int n) {
        int temp = m;
        m = n;
        n = temp;
        System.out.println(m + " " + n);
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        for (int i = 0; i < t; i++) {
            int m = sc.nextInt();
            int n = sc.nextInt();

            swap(m, n);
        }
        sc.close();
    }
}

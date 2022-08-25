import java.util.*;

public class ReverseTheArray {
    public static void reverseArray(ArrayList<Integer> arr, int m) {
        int n = arr.size();
        for (int i = m + 1, j = n - 1; j >= i; i++, j--) {
            Collections.swap(arr, i, j);
        }
    }
}

// 2
// 6 3
// 1 2 3 4 5 6
// 5 2
// 10 9 8 7 6

// 1 2 3 4 6 5
// 10 9 8 6 7
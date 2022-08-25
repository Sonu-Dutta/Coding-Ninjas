import java.util.ArrayList;
import java.util.*;

public class kthSmallestAndLargestElement {
    public static ArrayList<Integer> kthSmallLarge(ArrayList<Integer> arr, int n, int k) {
        Collections.sort(arr);
        ArrayList<Integer> num = new ArrayList<>();
        num.add(arr.get(k - 1));
        num.add(arr.get(n - k));
        return num;
    }
}
public class Sort012 {
    public static void sort012(int[] arr) {

        int n = arr.length;
        int one = 0, two = 0, zer = 0;
        for (int i = 0; i < n; i++) {
            if (arr[i] == 0)
                zer++;
            else if (arr[i] == 1)
                one++;
            else if (arr[i] == 2)
                two++;
        }
        for (int i = 0; i < zer; i++)
            arr[i] = 0;
        for (int i = 0; i < one; i++)
            arr[i + zer] = 1;
        for (int i = 0; i < two; i++)
            arr[i + zer + one] = 2;
    }
}
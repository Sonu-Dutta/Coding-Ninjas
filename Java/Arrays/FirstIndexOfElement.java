import java.util.Scanner;

class Solution {

    public int search(int arr[], int size, int x) {
        for (int i = 0; i < size; i++) {
            if (arr[i] == x) {
                return i;
            }
        }
        return -1;
    }
}

class FirstIndexOfElement {

    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int arr[] = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }
        int x = sc.nextInt();
        Solution s = new Solution();
        int res = s.search(arr, n, x);
        System.out.println(res);
        sc.close();
    }

}
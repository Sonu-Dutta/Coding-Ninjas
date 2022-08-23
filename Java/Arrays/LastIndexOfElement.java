import java.util.Scanner;

class LastIndexOfElement {
    public static void main(String args[]) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = in.nextInt();
        }
        int index = -1;
        int x = in.nextInt();
        for (int i = 0; i < n; i++) {
            if (x == arr[i]) {
                index = i;
            }
        }
        System.out.println(index);
        in.close();
    }

}

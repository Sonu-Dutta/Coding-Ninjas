
import java.util.Scanner;

class AreaOfRectangle {

    public static void main(String args[]) {

        Scanner sc = new Scanner(System.in);
        String input = sc.nextLine();
        String[] numbers = input.split(" ");

        int a1 = Integer.parseInt(numbers[0]);
        int b1 = Integer.parseInt(numbers[1]);
        int ans = a1 * b1;
        System.out.println(ans);

        sc.close();
    }
}

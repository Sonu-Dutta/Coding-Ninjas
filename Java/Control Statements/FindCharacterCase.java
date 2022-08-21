import java.util.Scanner;

class FindCharacterCase {
    public static void main(String args[]) {
        char s;
        Scanner sc = new Scanner(System.in);
        s = sc.next().charAt(0);
        if (Character.isUpperCase(s))
            System.out.println("1");
        else if (Character.isLowerCase(s))
            System.out.println("0");
        else
            System.out.println("-1");
        sc.close();
    }
}
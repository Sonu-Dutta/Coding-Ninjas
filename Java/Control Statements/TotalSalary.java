import java.util.*;

class TotalSalary {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        int salary = sc.nextInt();
        char grade = sc.next().charAt(0);
        if (salary >= 0 && salary <= 7500000) {
            double hra = 0.2 * salary;
            double da = 0.5 * salary;
            int allow;
            if (grade == 'A') {
                allow = 1700;
            } else if (grade == 'B') {
                allow = 1500;
            } else {
                allow = 1300;
            }
            double pf = 0.11 * salary;
            double totalsalary = salary + hra + da + allow - pf;
            System.out.println(Math.round(totalsalary));
        }
        sc.close();
    }
}

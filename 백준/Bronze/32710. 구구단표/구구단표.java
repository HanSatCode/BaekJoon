import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        sc.close();

        boolean t = false;

        if (n >= 1 && n <= 9)  t = true;
        else {
            for (int i = 2; i <= 9; i++) {
                if (n % i == 0 && (n / i) >= 1 && (n / i) <= 9) {
                    t = true;
                    break;
                }
            }
        }
        System.out.println(t ? "1" : "0");
    }
}

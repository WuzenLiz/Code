import java.util.Scanner;

public class prime {

    private static Boolean isPrime(int n) {
        if (n <= 1) {  
            return false;  
        }else{
            for (int i = 2; i < n; i++) {  
                if (n % i == 0) {  
                    return false;  
                }  
            }  
            return true;  
        }  
    }

    private static int input() {
        int n = 0;
        try {
            Scanner sc = new Scanner(System.in);
            n = sc.nextInt(); 
        }
        catch(Exception d) {
            Scanner sc = new Scanner(System.in);
            System.out.print("Nhập lỗi!\nHãy nhập lại!: ");
            n = sc.nextInt();
        }
        return n;
    }
    public static void main(String[] args) {
        int n=input();
        do {
            --n;
            if (isPrime(n)) {
                    System.out.print(n+"\t");
            }
        }while (0<n);
    }
}
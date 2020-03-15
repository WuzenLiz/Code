import java.util.*;
import java.lang.Math;

public class ToanHoc{
    /*--------------------Câu 1: Tính tổng: S=1!+2!+3!+...+n!------------*/
    //Tinh Giai Thừa (Sử Dụng Đệ quy)
    //Ý tưởng từ : n!=n*(n-1) từ wiki https://en.wikipedia.org/wiki/Factorial
    private static long GiaiThua(int i) {
        if (i<=2)
            return i;
        else
            return Math.abs(i*GiaiThua(i-1));
    }
    //Tính Tổng
    private static long TongGiaiThua(int n){
        long sum = 0;
        for (int i=1 ; i<=n ; i++) {
            sum += GiaiThua(i);
        }
        return sum;
    }

    /*--------------------Câu 2: Tính tổng: S2=1-1/3+1/5-1/7+1/9…------------*/
    //Ý tưởng từ: https://www.quora.com/Why-is-1-1-3-+-1-5-1-7-+-1-9-%CF%80-4
    //Từ ý tưởng ta có pi/4
    private static double TinhTongS2() {
        return Math.PI/4;
    }

    /*--------------------Câu 3: Giải hệ pt bậc nhất 2 ẩn------------*/
    //Ý tưởng: Luật Cramer link: https://www.intmath.com/matrices-determinants/1-determinants.php
    private static void tinh(float arr[][]){
        float temp = arr[0][0]*arr[1][1]-arr[0][1]*arr[1][0];
        if (temp==0){
            System.out.print("\nPhương trình vô nghiệm!");
        }else{
            float x=(arr[0][2]*arr[1][1]-arr[0][1]*arr[1][2])/temp;
            float y=(arr[0][0]*arr[1][2]-arr[0][2]*arr[1][0])/temp;
            System.out.println("\nNghiệm của hệ Phương trình đã nhập là:");
            System.out.printf("x=%.4f y=%.4f",x,y);
        }
    }

    /*--------------------Input------------*/
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
    /*-------------------*main*----------------*/
    public static void main(String[] args) {
        System.out.print("Nhập N: ");
        int n = input();
        float[][] a = new float[2][3];
        if (n<=20) {
            System.out.printf("Tổng giai thừa của "+n+" số là: S="+TongGiaiThua(n)+"\n");
        } else {
            System.out.println("OverFlow!!!!");
        }
        System.out.printf("Tổng dãy S2= %.5f\n",TinhTongS2()); 
        System.out.println("Nhập hệ phương trình 2 ẩn!");
        System.out.println("Nhập phương trình 1:");
        for (int i = 0; i < 3; i++) {
            System.out.print("a"+i+"= ");
            a[0][i]=input();
        }
        System.out.println("Nhập phương trình 2:");
         for (int i = 0; i < 3; i++) {
            System.out.print("b"+i+"= ");
            a[1][i]=input();
        }
        tinh(a);
    }
}
// [백준]14916번-자바-그리디-(거스름돈)-S5-(2-참고).java
// https://github.com/irishNoah/Algorithm-Study
// https://www.acmicpc.net/problem/14916

/*
dp로 안풀어서 그런 것 같다.
*/

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        int count = 0;
        
         while(true){
             if(N%5 == 0){
                    count += N/5;
                 System.out.println(count);
                 break;
             }else{
                 N -= 2;
                 count++;
             }
             if(N < 0){
                 System.out.println(-1);
                 break;
             }
         }
    }
}
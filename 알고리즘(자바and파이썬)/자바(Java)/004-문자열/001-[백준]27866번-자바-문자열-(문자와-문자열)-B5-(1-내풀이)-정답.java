// [백준]27866번-자바-문자열-(문자와-문자열)-B5-(1-내풀이)-정답.java
// https://github.com/irishNoah/Algorithm-Study
// https://www.acmicpc.net/problem/27866

/*

 */

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        String s = sc.next();
        int n = sc.nextInt();
        
        System.out.println(s.charAt(n-1));
        
    }
}

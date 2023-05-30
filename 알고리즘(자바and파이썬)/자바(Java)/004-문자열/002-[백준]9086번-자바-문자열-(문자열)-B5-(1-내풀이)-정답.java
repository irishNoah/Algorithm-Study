// [백준]9086번-자바-문자열-(문자열)-B5-(1-내풀이)-정답.java
// https://github.com/irishNoah/Algorithm-Study
// https://www.acmicpc.net/problem/9086

/*
ㅋㅋ.. while문을 써놓고 탈출 조건을 안써서 런타임 에러가 뜨게 만들다니... 조심히야겠다.
 */

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        int n = sc.nextInt();
        
        while(true) {
        	n = n-1;
        	
        	String s = sc.next();
        	
        	System.out.printf("%s%s", s.charAt(0), s.charAt(s.length()-1));
        	System.out.println();
        	
        	if(n == 0)
        		break;
        	
        }
    }   
}

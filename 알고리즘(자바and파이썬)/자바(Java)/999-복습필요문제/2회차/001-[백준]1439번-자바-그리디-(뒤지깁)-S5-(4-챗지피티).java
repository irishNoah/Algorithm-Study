// [백준]1439번-자바-그리디-(뒤지깁)-S5-(4-챗지피티).java
// https://github.com/irishNoah/Algorithm-Study
// https://www.acmicpc.net/problem/1439

/*

*/

import java.util.StringTokenizer;
import java.io.*;


public class Main {
    public static void main(String[] args) throws IOException {
    	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    	String str = br.readLine();
    	
    	System.out.println(seek(str));
    }
    
    private static int seek(String S) {
    	// 1의 개수를 새주는 게 아닌, 다른 문자가 나오기 전까지의 1로 이루어진 그룹수를 세워주는 느낌
    	StringTokenizer one = new StringTokenizer(S, "1"); 
    	// 위와 동
    	StringTokenizer zero = new StringTokenizer(S, "0");
    	
    	// 그룹수를 반환
    	int cntOne = one.countTokens();
    	int cntZero = zero.countTokens();
    	
    	return Math.min(cntOne, cntZero);
    }
}
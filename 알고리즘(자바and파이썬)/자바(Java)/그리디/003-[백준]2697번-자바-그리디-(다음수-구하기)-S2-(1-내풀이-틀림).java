// [백준]2697번-자바-그리디-(다음수-구하기)-S2-(1-내풀이-절반).java
// https://github.com/irishNoah/Algorithm-Study
// https://www.acmicpc.net/problem/2697

/*
대부분의 테스트 케이스가 맞았으나
일부 테스트 케이스에서 실패했다.
즉, 초반 설계를 잘 못한 듯....
*/

import java.io.*;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) throws IOException {
        
    	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    	String many = br.readLine();
    	int test = Integer.parseInt(many);
    	
    	
    	while(true) {
    		test = test-1;
    				
    		String value = br.readLine();
    		
    		result(value);
    		
		if(test == 0) break;
    	}
    	
    }

    	// 다음수 구하기
	private static void result(String value) {
		char arr[] = value.toCharArray();
		
		String coin ="";
		int check = 0;
		
		// 다음수가 있을지 판별
		for(int i = arr.length-1; i >= 1; i--) {			
			
			if (arr[i-1] < arr[i]) {
				coin = String.valueOf(arr[i]);
				check = i;
				
				break;
			}
		}
		
		// 다음수가 없는 경우
		if (coin == "") {
			System.out.println("BIGGEST");
		}
		
		// 다음수가 있는 경우
		else {
			
			String sol;
			sol = value.substring(check-1, check); // coin 바로 앞 수
			sol += value.substring(check+1); // coin 뒤에 있는 모든 수
			
			char res[] = sol.toCharArray();
			Arrays.sort(res);
			
			// char형 배열 문자열로 변환
			String strRes = new String(res);
			// 리턴값 구하기
			strRes = value.substring(0, check-1) + coin + strRes;
			
			System.out.println(strRes);
		}
		
		
		
	}
}
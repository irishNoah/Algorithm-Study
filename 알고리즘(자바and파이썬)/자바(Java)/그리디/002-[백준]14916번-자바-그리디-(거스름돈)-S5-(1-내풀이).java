// [백준]14916번-자바-그리디-(거스름돈)-S5-(1-내풀이).java
// https://github.com/irishNoah/Algorithm-Study
// https://www.acmicpc.net/problem/14916

/*
이클립스에서는 잘 됐는데, 백준에서는 틀린 판정이 났다.
다른 분들의 풀이를 참고해서 내가 왜 틀렸는지 분석을 해봐야 겠다. 
*/

import java.io.*;


public class Main {
    public static void main(String[] args) throws Exception {
    	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    	
    	int num = Integer.parseInt(br.readLine());
    	result(num);
    }
    
    static void result(int num) {
    	if (num == 1 || num == 3) {
    		System.out.println(-1);
    		System.exit(0);
    	}
    	
    	int cnt = 0; 
    	
    	int rest = Math.floorMod(num, 10);
    	
    	if (rest == 1 || rest == 3 || rest == 5 || rest == 7 || rest == 9) {
    		if (rest == 1 || rest == 6) {
    			num -= 6;
    			cnt += num / 5;
    			cnt += 3;
    		}
    		if (rest == 3 || rest == 8)  {
    			num -= 8;
    			cnt += num / 5;
    			cnt += 4;
    		}
    		if (rest == 5) {
    			num -= 10;
    			cnt += num / 5;
    			cnt += 5;
    		}
    		
    	}
    	
    	else {
    		cnt += num / 5;
    		
    		num = num - (cnt)*5;
    		
    		cnt += num / 2;
    	}
    	
    	System.out.println(cnt);
    }
    
}
// [백준]2798-자바-브루트포스-(블랙잭)-B2-(2-참고-정답)-브루트포스.java
// https://github.com/irishNoah/Algorithm-Study
// https://www.acmicpc.net/problem/2798

/*
*** 제한 > 시간 : 1초 (기본 1초) / 메모리 : 128MB (기본 128MB)

*** 조건
- 문자열 s에는 둘 이상의 정수가 공백으로 구분되어 있다.


* 설계 [총 14분 소요] / 총 풀이 시간[총 -분 소요]


*/

import java.io.*;
import java.util.*;
import java.lang.Math;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        String s = br.readLine();
        String[] str = s.split(" ");
        
        int N = Integer.parseInt(str[0]); // 카드수
        int M = Integer.parseInt(str[1]); // 최대합
        
        // 카드 입력 후 구분
        String c = br.readLine();
        String[] card = c.split(" ");
        
        // 정수형 타입으로 변환
        List<Integer> arr = new ArrayList<>();
        
        for(String val : card) {
        	arr.add(Integer.parseInt(val));
        }
        
        int res = 0;
        
        	
    	for (int i = 0; i <= arr.size()-3; i++) {
    		
    		for(int j = i+1; j <= arr.size()-2; j++) {
    			
    			for(int k = j+1; k <= arr.size()-1; k++) {
    				int sum = arr.get(i) + arr.get(j) + arr.get(k);
    				
    				if (sum <= M) {
    					res = Math.max(res, sum);
    				}
    				if (res == M) {
    					System.out.println(res);
    					return;
    				}
    					
    			}
    			
    		}
    		
    	}
        
    	System.out.println(res);
        	
        
    }
}

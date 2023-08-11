// [백준]15650-자바-브루트포스-(N과-M-(2))-S3-(2-참고-정답)-백트래킹.java
// https://github.com/irishNoah/Algorithm-Study
// https://www.acmicpc.net/problem/15650

/*
*** 제한 > 시간 : 1초 (기본 1초) / 메모리 : 128MB (기본 128MB)

*** 조건
- 문자열 s에는 둘 이상의 정수가 공백으로 구분되어 있다.


* 설계 [총 14분 소요] / 총 풀이 시간[총 -분 소요]
> 참고 URL : https://st-lab.tistory.com/115

*/

import java.io.*;
import java.util.*;

public class Main {
	
	// 전역 변수에 때려 박아
	public static int N;
	public static int M;
	public static int[] arr;
	//public static boolean[] visit;
	public static StringBuilder sb = new StringBuilder();
	
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        String s = br.readLine();
        String str[] = s.split(" ");
        
        N = Integer.parseInt(str[0]);
        M = Integer.parseInt(str[1]);
        
        arr = new int[M];
        //visit = new boolean[N];
        
        dfs(1, 0);
        System.out.println(sb);
        
    }
    
    
    public static void dfs(int start, int depth) { 
    	
    	// 조건
    	if (depth == M) {
    		for(int val : arr) {
    			sb.append(val).append(" ");
    		}
    		sb.append("\n");
    		//start += 1; // 시작 지점 1 증가
    		return;
    	}
    	
    	
    	// 수행
    	// i는 start부터 탐색하도록 한다.
    	for (int i = start; i <= N; i++) {
    		// 현재 깊이를 index로 하여 해당 위치에 i 값을 담는다
    		arr[depth] = i;
    		
    		/*
    		재귀호출 :
		 	현재 i 값보다 다음 재귀에서 더 커야하므로
		 	i + 1 의 값을 넘겨주고, 깊이 또한 1 증가시켜 재귀호출해준다 
    		 */
    		dfs(i+1, depth+1);
    	}
    	
    }
    
}

// [백준]15649-자바-브루트포스-(N과-M-(1))-S3-(1-내풀이-정답)-백트래킹.java
// https://github.com/irishNoah/Algorithm-Study
// https://www.acmicpc.net/problem/15649

/*
*** 제한 > 시간 : 1초 (기본 1초) / 메모리 : 128MB (기본 128MB)

*** 조건
- 문자열 s에는 둘 이상의 정수가 공백으로 구분되어 있다.


* 설계 [총 14분 소요] / 총 풀이 시간[총 -분 소요]


*/

import java.io.*;
import java.util.*;

public class Main {
	
	// 전역 변수에 때려 박아
	public static int N;
	public static int M;
	public static int[] arr;
	public static boolean[] visit;
	public static StringBuilder sb = new StringBuilder();
	
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        String s = br.readLine();
        String[] str = s.split(" ");
        
        // 전역변수 N과 M 초기화
        N = Integer.parseInt(str[0]);
        M = Integer.parseInt(str[1]);
        
        arr = new int[M];
        visit = new boolean[N];
        
        dfs(0);
        System.out.println(sb);
    }
    
    
    public static void dfs(int depth) { 
    	
    	// 리턴 조건
    	if(depth == M) {
    		for (int val : arr) {
    			sb.append(val).append(' ');
    		}
    		sb.append('\n');
    		return;
    	}
    	
    	// 수열 생성
    	for (int i = 0; i < N; i++) {
    		if (!visit[i]) {
    			visit[i] = true;
    			arr[depth] = i+1;
    			dfs(depth+1);
    			visit[i] = false; // 리턴 됐을 경우 이 자리로 복귀
    		}
    	}
    	
    }
    
}

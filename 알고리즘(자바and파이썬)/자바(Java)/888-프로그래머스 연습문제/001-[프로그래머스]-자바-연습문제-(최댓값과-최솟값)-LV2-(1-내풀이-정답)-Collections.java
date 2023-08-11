// [프로그래머스]-자바-연습문제-(최댓값과-최솟값)-LV2-(1-내풀이-정답)-Collections.java
// https://github.com/irishNoah/Algorithm-Study
// https://school.programmers.co.kr/learn/courses/30/lessons/12939

/*
*** 제한 > 시간 : ?초 (기본 1초) / 메모리 : ?MB (기본 128MB)

*** 조건
- 문자열 s에는 둘 이상의 정수가 공백으로 구분되어 있다.


* 설계 [총 -분 소요] / 총 풀이 시간[총 -분 소요]
- s를 공백으로 구분한 이후 각 값을 정수형으로 치환한 리스트 arr에 할당
- Collections를 사용하여 최소값 및 최대값 찾고 반환

*/

import java.util.*;
//import java.lang.Math;


public class Solution {

	public static String solution(String S) {
		String answer = "";
			
		String[] str = S.split(" "); // 공백 구분
		List <Integer> list = new ArrayList<>();
		
		for(String cmp : str) {
			list.add(Integer.parseInt(cmp));
		}
		
		int valMax = Collections.max(list);
		int valMin = Collections.min(list);
		
		answer = Integer.toString(valMin) + " " + Integer.toString(valMax);
		
		return answer;
		
	}
	
	
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		// 예제 1
		String S = "1 2 3 4";
		System.out.println(solution(S)); // "1 4"
		
		
		// 예제 2
		String S1 = "-1 -2 -3 -4";
		System.out.println(solution(S1)); // "-4 -1"
		
		// 예제 3
		String S2 = "-1 -1";
		System.out.println(solution(S2)); // "-1 -1"		
			
	}

}

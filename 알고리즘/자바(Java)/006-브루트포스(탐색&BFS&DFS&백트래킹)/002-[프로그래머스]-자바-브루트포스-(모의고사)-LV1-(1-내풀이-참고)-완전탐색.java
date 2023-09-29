// [프로그래머스]-자바-브루트포스-(모의고사)-LV1-(1-내풀이-참고)-완전탐색.java
// https://github.com/irishNoah/Algorithm-Study
// https://school.programmers.co.kr/learn/courses/30/lessons/42840?language=java

/*
*** 제한 > 시간 : ?초 (기본 1초) / 메모리 : ?MB (기본 128MB)

*** 조건
- 문자열 s에는 둘 이상의 정수가 공백으로 구분되어 있다.


* 설계 [총 -분 소요] / 총 풀이 시간[총 -분 소요]


*/

import java.util.*;
import java.lang.Math;


public class Solution {

	public static int[] solution(int[] answers) {
			
		int[] first = {1,2,3,4,5}; // 5개씩 반복
        int[] second = {2,1,2,3,2,4,2,5}; // 8개씩 반복
        int[] third = {3,3,1,1,2,2,4,4,5,5}; // 10개씩 반복
        int[] score = {0,0,0}; // 각 수포자들의 점수
        
        // 수포자들의 점수 계산
        for(int i=0; i<answers.length; i++) {
            if(answers[i] == first[i%5]) score[0]++;
            if(answers[i] == second[i%8]) score[1]++;
            if(answers[i] == third[i%10]) score[2]++;
        }
        
        // 최대 점수 구하기
        int max = Math.max(score[0], Math.max(score[1], score[2]));
        
        // 최대 점수를 가진 수포자 리스트 생성
        List<Integer> answ = new ArrayList<Integer>();
        for(int i=0; i<score.length; i++) if(max == score[i]) answ.add(i+1);
        
        int[] answer = new int[answ.size()];
        for(int i=0; i<answ.size(); i++){
            answer[i] = answ.get(i);
        }

        return answer;
		
	}
	
	
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		// 예제 1
		int[] answers1 = {1,2,3,4,5};
		System.out.println(solution(answers1)); // [1]
		
		
		// 예제 2
		int[] answers2 = {1,3,2,4,2};
		System.out.println(solution(answers2)); // [1, 2, 3]	
			
	}

}

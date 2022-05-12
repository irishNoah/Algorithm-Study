/*
 * 프로그래머스 LV1 - 모의고사(첫 번째 풀이) 
 * 분류 - 완전탐색
 * https://programmers.co.kr/learn/courses/30/lessons/42840
 * 
 * 정확성 테스트의 케이스 14개 중 6개 성공 
 * 효율성 테스트는 없었음 
 * 총점 42.9
 */

class Solution {
    public int[] solution(int[] answers) {
    	// answers의 길이를 구하기 위한 answer_length
		int answer_length = answers.length;
		
		// 수포자 1,2,3이 찍는 방식을 대입한 배열 human01, human02, human03
		int human01[] = {1, 2, 3, 4, 5};
		int human02[] = {2, 1, 2, 3, 2, 4, 2, 5}; 
		int human03[] = {3, 3, 1, 1, 2, 2, 4, 4, 5, 5}; 
		
		// 배열 human01~03의 길이를 각각 구한 human01_length, human02_length, human03_length
		int human01_length = human01.length, human02_length = human02.length, human03_length = human03.length;
		
		// 각 수포자가 맞춘 개수를 구하기 위한 cnt_human01~03
		int cnt_human01 = 0, cnt_human02 = 0, cnt_human03 = 0;
		
		// answer_length의 길이가 human01_length~human03_length의 길이보다 작을 경우를 대비한 j
		int j = 0;
	 
		//answer_length가 human01_length보다 작거나 같을 경우 다음 if문 수행
		if(answer_length <= human01_length) {
			for(int i = 0; i < answer_length; i++) {
				if(answers[i] == human01[i]) {
					cnt_human01++;
				}
			}
		}
		
		//answer_length가 human01_length보다 클 경우 다음 if문 수행
		if(answer_length > human01_length) {
			for(int i = 0; i < answer_length; i++) {
				if(answers[i] == human01[j]) {
					cnt_human01++;
				}
				
				j++;
				
				if(j == human01_length) {
					j = 0;
				}
			}	
		}
		
		//answer_length가 human02_length보다 작거나 같을 경우 다음 if문 수행
		if(answer_length <= human02_length) {
			for(int i = 0; i < answer_length; i++) {
				if(answers[i] == human02[i]) {
					cnt_human02++;
				}
			}
		}
		
		//answer_length가 human02_length보다 클 경우 다음 if문 수행
		if(answer_length > human02_length) {
			for(int i = 0; i < answer_length; i++) {
				if(answers[i] == human02[j]) {
					cnt_human02++;
				}
				
				j++;
				
				if(j == human01_length) {
					j = 0;
				}
			}	
		}
		
		//answer_length가 human03_length보다 작거나 같을 경우 다음 if문 수행
		if(answer_length <= human03_length) {
			for(int i = 0; i < answer_length; i++) {
				if(answers[i] == human03[i]) {
					cnt_human03++;
				}
			}
		}
		
		//answer_length가 human02_length보다 클 경우 다음 if문 수행
		if(answer_length > human03_length) {
			for(int i = 0; i < answer_length; i++) {
				if(answers[i] == human03[j]) {
					cnt_human03++;
				}
				
				j++;
				
				if(j == human01_length) {
					j = 0;
				}
			}	
		}

		int max_value = 0;
		
		int[] answer = {};
		
		// 만약 cnt_human01, cnt_human02, cnt_human03이 동일할 경우
		if(cnt_human01 == cnt_human02 && cnt_human01 == cnt_human03) {
			int[] answer_ck = new int[3];
			answer_ck[0] = 1;
			answer_ck[1] = 2;
			answer_ck[2] = 3;
			
			answer = answer_ck;
		}
		
		// 만약 cnt_human01, cnt_human02, cnt_human03 중 가장 많이 맞춘 인원이 따로 있을 경우
		else {
			int[] answer_ck = new int[1];
			max_value = Math.max(cnt_human01, cnt_human02);
			max_value = Math.max(max_value, cnt_human03);
			
			if(max_value == cnt_human01) {
				answer_ck[0] = 1;
			}
			else if(max_value == cnt_human02) {
				answer_ck[0] = 2;
			}
			else if(max_value == cnt_human03) {
				answer_ck[0] = 3;
			}
			
			answer = answer_ck;
		}
		
		// answer 리턴
		return answer;
    }
}
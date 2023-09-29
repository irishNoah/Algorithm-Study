// [프로그래머스]-자바-힙-(더-맵게)-LV2-(1-내풀이-정답)-최소힙.java
// https://github.com/irishNoah/Algorithm-Study
// https://www.acmicpc.net/problem/1874

/*
*** 제한 > 시간 : ?초 (기본 1초) / 메모리 : ?MB (기본 128MB)

*** 조건
- 2 <= scoville <= 백만
- 모든 음식의 스코빌 지수를 K 이상으로 만들 수 없는 경우에는 -1 리턴

* 설계 [총 -분 소요] / 총 풀이 시간[총 -분 소요]
- scoville에 대해 최소힙 구현
- 조건에 맞게 구현

*/

import java.util.*;


public class Solution {

	public static int solution(int [] scoville, int K) {
		int answer = 0;
		
		// 최소 힙 구현
		PriorityQueue<Integer> pq = new PriorityQueue<>();
		
		for (int num : scoville) {
			pq.add(num);
		}
		
		while (pq.peek() < K) { // 루트 노드가 K 이상일 때까지 진행
			// 만약, 다 섞어서 음식이 1개 밖에 안됐는데, 이 음식마저 K 미만이면 -1 리턴
			if (pq.size() == 1 && pq.peek() < K) { // peek() > 루트노드 값 / 반환은 하지 않음
				answer = -1;
				break;
			}
			
			int min1 = pq.poll(); // poll() > 루트노드 값 / 반환까지 함
			int min2 = pq.poll();
			int mix = min1 + (2*min2);
			
			pq.add(mix);
			answer += 1;

		}
			
		
		return answer;
		
	}
	
	
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		//List<Integer> scoville = new ArrayList<>();
		
		int scoville[] = {1,2,3,9,10,12};
		int K = 7;
		System.out.println(solution(scoville, K));
		
	}

}

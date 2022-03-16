/*
 * 프로그래머스 LV1 - 3진법 뒤집기(두 번째 풀이) 
 * 분류 - 월간 코드 챌린지 시즌1
 * https://programmers.co.kr/learn/courses/30/lessons/68935
 * 
 * 정확성 테스트의 케이스 10개 중 10개 성공 
 * 효율성 테스트는 없었음 총점 100.0
 */
 
//해당 문제는 다 Integer의 메소드만 사용해서 풀었다. 첫 번째 풀이보다 실행 기간이 비약적으로 줄어들었다.
class Solution {
    public int solution(int n) {
       int answer = 0;
       
       String ten_to_three = "";
       
       // 10진수 n을 3진법으로 변환해서 ten_to_three에 대입
       ten_to_three = Integer.toString(n, 3);

       	// 구해진 3진법 ten_to_three를 뒤집기 위해 StringBuffer를 활용
   		StringBuffer sb = new StringBuffer(ten_to_three);
   		String reverse_ten_to_three = sb.reverse().toString();
       
   		
   		answer = Integer.parseInt(reverse_ten_to_three, 3);
   		
       return answer;
    }
}
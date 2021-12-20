import java.util.Arrays;
import java.util.Collections;
class Solution {
    public String solution(String s) {
        
        //문자열 s의 요소가 영문으로만 이루어지기 확인하기 위한 checkS 변수 선언 
		char checkS;
		
		//문자열 s의 요소 확인
		for(int i = 0; i < s.length(); i++) {
			checkS = s.charAt(i);
			
			if(checkS >= 'a' && checkS <= 'z') {
				//소문자 ok
			}
			else if(checkS >= 'A' && checkS <= 'Z') {
				//대문자 ok
			}
			else {
				//영문 대,소문자가 아닌 다른 문자가 포함되어 있으면 시스템 강제 종료
				System.out.println("문자열 s에 영어 대,소문자가 아닌 다른 문자가 있습니다.");
				System.exit(0);
			}	
		}
		
		//영문으로만 이루어져있을시
		//문자열 s를 문자열 배열로 변환시키기 위한 문자열 배열 changeS 변수 선언
		char[] changeS = s.toCharArray();
		//changeS를 내림차순 정렬
		Arrays.sort(changeS);
		
	//char형 배열을 문자열처럼 출력하기 위헤 StringBuilder의 변수명 answer 선언
		StringBuilder answerBuilder = new StringBuilder(new String(changeS));
		String answer = answerBuilder.reverse().toString();
		return answer;
    }
}
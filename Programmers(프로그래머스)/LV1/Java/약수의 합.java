import java.util.*;

class Solution {
    public int solution(int n) {
        //n이 어떤 수냐에 따라 약수가 상이하므로, 배열의 길이를 미리 줄 수 없다.
				//따라서 우선 ArrayList를 선언한다.
				ArrayList <Integer> list = new ArrayList<>();
        
        //약수는 1부터 시작됨으로, i = 1 부터 시작
				for(int i = 1; i <= n; i++) {
					if(n % i == 0) {
						//n % i == 0일 경우 i는 n의 약수이므로
						//list에 추가를 해준다. 단 list는 ArrayList type이므로
						//i를 Integer로 강제 type 변환 해준다.
						list.add((Integer)i);
					}
				}
        
        //정수형 배열 arr 선언
				//size는 ArrayList 변수명 list의 size를 넣어준다.
				int[] arr = new int[list.size()];
				
				//arr[i]에 list에 있는 값을 get() 메소드를 통해 대입해준다.
				for(int i = 0; i < arr.length; i++) {
					arr[i] = list.get(i);
				}
        
        
        int answer = 0;
        for(int i = 0; i < arr.length; i++) {
					answer += arr[i];
				}
        
        return answer;
    }
}
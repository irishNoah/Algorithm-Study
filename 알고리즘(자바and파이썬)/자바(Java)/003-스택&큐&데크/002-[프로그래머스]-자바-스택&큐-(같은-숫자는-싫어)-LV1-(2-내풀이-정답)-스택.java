// [프로그래머스]-자바-스택&큐-(같은-숫자는-싫어)-LV1-(2-내풀이-정답)-스택.java
// https://github.com/irishNoah/Algorithm-Study
// https://school.programmers.co.kr/learn/courses/30/lessons/12906

/*
# 스택으로 푼다

1. 스택 생성
2. 스택에 차례대로 arr의 요소를 할당
    - 스택이 비어있다면
        - 그냥 그 요소 할당 및 continue
    - 이 요소가 스택에 마지막으로 넣어진 값과 다를 경우에만
        - 이 요소 할당
3. 스택을 문자열로 치환해서 반환 (반환 타입 변환해주기!!!)

*/

import java.util.*;

public class Solution {
    public Object[] solution(int []arr) { // public int[] solution(int []arr)
        
        Stack<Integer> st = new Stack<>();
        
        for (int num : arr){
            if (st.empty() == true) {
                st.push(num);
                continue;
            }
            
            if (st.peek() != num){
                st.push(num);
            }
        }

        Object[] answer = st.toArray();
        
        return answer;
    }
}
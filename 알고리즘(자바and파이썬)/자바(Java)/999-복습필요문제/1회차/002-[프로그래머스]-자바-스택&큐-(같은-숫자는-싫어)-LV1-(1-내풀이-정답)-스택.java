// [프로그래머스]-자바-스택&큐-(같은-숫자는-싫어)-LV1-(1-내풀이-정답)-스택.java
// https://github.com/irishNoah/Algorithm-Study
// https://school.programmers.co.kr/learn/courses/30/lessons/12906

/*
*** 제한 > 시간 : ?초 (기본 1초) / 메모리 : ?MB (기본 128MB)

*** 조건

*** 설계 [총 12분 소요] / 총 풀이 시간[총 29분 소요]
- 스택으로 구현했다.
    - 정답 이후 다른 분들은, 그냥 ArrayList 활용 하더라궁
- 뭐, 암튼 스택 문제니 잘 푼 것 같기는 하다!

*** 다음에 풀 때는?
- 내가 여기서 29분 걸린 이유는 스택으로 구현하고 나서, 반환 타입을
스택이 아닌 정수형 타입의 배열로 반환해야 되기 때문에, 애를 먹었기 때문이다.
- 만약, 스택 구현을 스택이 아닌 리스트를 활용해서 했다면
    - 정수형 배열 = 리스트.toArray(); 를 활용해서 리턴하면 됐다.
- 하지만, 스택 구현을 스택으로 했기 때문에 toArray() 가 불가능
    - 그럼, 아예 불가능? ㄴㄴ
        - 반환 타입을 int[]가 아닌 Object[]로 바꾸어준다.  
            - 그러면 스택.toArray() 가 가능하다!!!!!
*/

import java.util.*;

public class Solution { 
    public Object[] solution(int []arr) { // 반환 타입을 Object[]로 변환
        Stack<Integer> st = new Stack<>();
        
        st.push(arr[0]); // 첫 번째 원소는 할당
        
        
        for (int i = 1; i < arr.length; i++){
            
            // 최근에 추가했던 원소와 이번에 넣어볼 원소를 비교
            if (st.peek() != arr[i]){ // 다를 경우에만 스택에 넣어줌
                st.push(arr[i]);
            }
        }
        
        // 구현한 스택을 Object[]에 toArray() 해서 반환
        Object [] answer = st.toArray();

        return answer;
    }
}
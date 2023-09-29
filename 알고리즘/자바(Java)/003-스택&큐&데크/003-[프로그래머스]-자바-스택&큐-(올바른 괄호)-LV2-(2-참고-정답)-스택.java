// [프로그래머스]-자바-스택&큐-(올바른 괄호)-LV2-(2-참고-정답)-스택.java
// https://github.com/irishNoah/Algorithm-Study
// https://school.programmers.co.kr/learn/courses/30/lessons/42840?language=java

/*
*** 제한 > 시간 : ?초 (기본 1초) / 메모리 : ?MB (기본 128MB)

*** 조건
- 문자열 s에는 둘 이상의 정수가 공백으로 구분되어 있다.


*** 설계 [총 -분 소요] / 총 풀이 시간[총 -분 소요]

*** 분석
- 자바는 참 타입이...
- 문자열 to Char 형 배열 (https://adjh54.tistory.com/189)
    - char[] arr = s.toCharArray();

*** 참고 URL
> https://velog.io/@doxxx93/practice-kit-stack-queue-1
*/

import java.util.*;  
  
class Solution {  
  
    boolean solution(String s) {  
        Stack<Character> stack = new Stack<>();  
        for (int i = 0; i < s.length(); i++) {  
            if (s.charAt(i) == '(') {  
                stack.push('(');  
            } else if (s.charAt(i) == ')') {  
                if (stack.isEmpty()) {  
                    return false;  
                }  
                stack.pop();  
            }  
        }  
        return stack.isEmpty();  
    }  
}
// [프로그래머스]-자바-스택&큐-(올바른 괄호)-LV2-(1-내풀이-75점)-스택.java
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


*/

import java.util.*;

class Solution {
    boolean solution(String s) {
        boolean answer = true;

        List<String> list = new ArrayList<>();
        
        // 문자열을 char 형 배열에 담음
        char[] arr = s.toCharArray();
        
        // arr이 char 타입이므로, String.valueOf()를 통해
        // char형 타입을 String 타입으로 변환해줘야 한다.
        list.add(String.valueOf(arr[0]));
        
        for (int i = 1; i < arr.length; i++){
            // 마지막 요소가 있는지 체크하기 위해 사이즈 변수 구함
            int size = list.size();
            System.out.println("size = " + size);
            
            // 리스트가 비어있을 대
            if (size == 0){
                System.out.println("111111");
                
                if(arr[i] == '('){
                    list.add(String.valueOf(arr[i]));
                }
                else{
                    answer = false;
                    return answer;
                }
            }
            
            // 리스트가 비어있지 않을 때
            else{ // 마지막 요소와 비교한다.
                System.out.println("22222");
                System.out.println(list.get(size-1));
                
                // arr[i-1] == '('
                if (arr[i-1] == '('){ // list의 마지막이 "(" 이면
                    if (arr[i] == '('){
                        System.out.println("33333");
                        list.add(String.valueOf(arr[i]));
                    }
                    else{
                        // 마지막 값 제거
                        System.out.println("44444");
                        list.remove(size-1);
                    }
                }
                else{ // list의 마지막이 ")" 이면
                    System.out.println("55555");
                    answer = false;
                    return answer;
                }
            }
        }
        
        // 위에서 문제가 없었을 때 길이가 0이 아니면 올바른 괄호가 아님
        int leng = list.size();
        System.out.println("leng = " + leng);
        
        if (leng != 0){
            answer = false;
        }
        
        // 즉, 최종 길이가 0이여야만 true        
        return answer;
    }
}
// [프로그래머스]-자바-브루트포스-(모의고사)-LV1-(2-내풀이-성공)-완전탐색.java
// https://github.com/irishNoah/Algorithm-Study
// https://school.programmers.co.kr/learn/courses/30/lessons/42840?language=java

/*
1. 수포자 1,2,3이 찍는 방식을 담은 각 배열을 생성
    - 수포자 1(pOne)은 찍는 루틴이 5개 
    - 수포자 2(pTwo)은 찍는 루틴이 8개
    - 수포자 3(pThree)은 찍는 루틴이 10개
2. for문으로 answers를 돌며
    - 수포자 1 > pOne[i % 5] == answers[i] >>> cnt1 += 1
    - 수포자 2 > pTwo[i % 8] == answers[i] >>> cnt2 += 1
    - 수포자 3 > pThree[i % 10] == answers[i] >>> cnt3 += 1
3. cnt1,cnt2,cn3 중 max 값을 담은 변수 val에 생성
4. val과 cnt1~cnt3를 비교해서 리턴 배열에 담아주고 리턴
*/

import java.util.*;
import java.lang.*;

class Solution {
    public int[] solution(int[] answers) {
        //int[] answer = {};
        
        int[] pOne = {1, 2, 3, 4, 5}; // 5개
        int[] pTwo = {2, 1, 2, 3, 2, 4, 2, 5}; // 8개
        int[] pThree = {3, 3, 1, 1, 2, 2, 4, 4, 5, 5}; //10개
        
        // 각 인원마다 몇 개 맞았는지 구하기
        int cnt1 = 0, cnt2 = 0, cnt3 = 0;
        for (int i = 0; i < answers.length; i++){
            if (answers[i] == pOne[i % 5]){
                cnt1 += 1;
            }
            if (answers[i] == pTwo[i % 8]){
                cnt2 += 1;
            }
            if (answers[i] == pThree[i % 10]){
                cnt3 += 1;
            }
        }
        
        // 최대값 구하기
        int val = Math.max(cnt1, Math.max(cnt2, cnt3));
        
        // 최대값과 동일한 개수를 맞춘 인원이 몇 명 있는가 구하기
        int cmp = 0;
        if (cnt1 == val) cmp+= 1;
        if (cnt2 == val) cmp+= 1;
        if (cnt3 == val) cmp+= 1;
        
        // 결과 배열 생성 및 처리
        int[] res = new int[cmp];
        int num = 0;
        while (cmp != num){
            if (cnt1 == val){
                res[num] = 1;
                num ++;    
            }
            if (cnt2 == val){
                res[num] = 2;
                num ++;    
            }
            if (cnt3 == val){
                res[num] = 3;
                num ++;    
            }
        
        }
        
        return res;
    }
}
'''
032-[프로그래머스]-구현-(스킬트리)-LV2-(2-다른풀이).py

### 주소
> https://school.programmers.co.kr/learn/courses/30/lessons/49993

### 참고
> 없음

### 설계 -분, 총 -분
 
'''

def solution(skill,skill_tree):
    answer=0
    
    for i in skill_tree: # skill_tree의 각 단어에 대해서
        skillist=''
        for z in i: # 각 단어의 알파벳에 대해서
            if z in skill: # 특정 알파벳이 skill 안에 있을 때
                skillist+=z # skillist라는 문자열에 특정 알파벳을 더해줌
        
        # 최종적으로 구해진 skillist이 skill의 구성요소와 시작하는 부분이
        # 정답 1 증가. 즉, startswith와 비슷한 것을 슬라이싱으로 했다고 보면 됨
        if skillist==skill[0:len(skillist)]:
            answer+=1
    return answer
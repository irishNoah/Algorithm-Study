'''
032-[프로그래머스]-구현-(스킬트리)-LV2-(1-내풀이).py

### 주소
> https://school.programmers.co.kr/learn/courses/30/lessons/49993

### 참고
> 없음

### 설계 10분, 총 30분
1. skill = list(skill) >>> skill 리스트화
2. skill_trees 돌기
    - skill의 길이에 맞는 result = [False] * len(skill) 생성
        - 왜냐하면 각 skill_trees의 단어에 대해서 계속 검수해야 하니깐!
    - flag = True >>> 스킬 트리 판별 여부
    - 각 skill_trees의 요소가 skill에 없는 경우는 pass
    - 있는 경우에는?
        - skill.index(요소)가 0인 경우에는
            - result[skill.index(요소)] = True
            - continue
        - 그렇지 않을 경우에는
            - 앞선 요소가 True인지 먼저 체크
                - if result[skill.index(요소) - 1] == True:
                    - result[skill.index(요소)] == True
                - 근데 거짓이야?
                    - flag = False
                    - break
    - 만약, flag가 True일 경우에는?
        - answer += 1
4. 리턴 answer
 
 
'''

def solution(skill, skill_trees):
    answer = 0
    
    skill = list(skill) # 필수 수강 과목
    
    for val in skill_trees:
        result = [False] * len(skill) # 매 단어 검수
        
        arr = list(val)
        flag = True
        
        for alp in arr:
            # 필수 수강 과목이 아닌 것은 pass
            if alp not in skill:
                continue
            
            # # 필수 수강 과목에 대해서만 check
            if skill.index(alp) == 0:
                result[skill.index(alp)] = True
    
            else:
                if result[skill.index(alp)-1] == True:
                    result[skill.index(alp)] = True
                else:
                    flag = False
                    break
        
        # 문제 없이 들은 것에 대해서만 답 1개 증가
        if flag == True:
            answer += 1
    
    return answer
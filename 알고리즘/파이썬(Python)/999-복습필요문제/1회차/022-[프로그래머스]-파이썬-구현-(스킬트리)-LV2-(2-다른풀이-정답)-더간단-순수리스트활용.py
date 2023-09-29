# [프로그래머스]-파이썬-구현-(스킬트리)-LV2-(2-다른풀이-정답)-더간단-순수리스트활용.py
# https://github.com/irishNoah/Algorithm-Study
# https://school.programmers.co.kr/learn/courses/30/lessons/49993

'''
*** 제한 > 시간 : ?초 (기본 1초) / 메모리 : ?MB (기본 128MB)


*** 조건
> 스킬은 알파벳 대문자로 표기하며, 모든 문자열은 알파벳 대문자로만 이루어져 있습니다.
> 스킬 순서와 스킬트리는 문자열로 표기합니다.
    > 예를 들어, C → B → D 라면 "CBD"로 표기합니다
> 선행 스킬 순서 skill의 길이는 1 이상 26 이하이며, 스킬은 중복해 주어지지 않습니다.
> skill_trees는 길이 1 이상 20 이하인 배열입니다.
> skill_trees의 원소는 스킬을 나타내는 문자열입니다.
    > skill_trees의 원소는 길이가 2 이상 26 이하인 문자열이며, 스킬이 중복해 주어지지 않습니다.

* 설계 [총 -분 소요] / 총 풀이 시간[총 -분 소요]
-

* 나와의 차이
- 동일하게 for문을 활용했지만, 나 같은 경우에는 dict()를 활용했단 점으로 조금 더 길어졌다.
- 이 사람은 순수 리스트 안에 있는 것만 활용했다.

'''
#===================================================================================

def solution(skill,skill_tree):
    answer=0

    for i in skill_tree:
        skillist=''

        for z in i:
            if z in skill:
                skillist+=z

        # 문제에서는 skill 안에 있는 요소들이 다 나오는 것이 아니라
        # skill의 일부여도 순서만 맞으면 answer에 반영된다.
        if skillist==skill[0:len(skillist)]:
            answer+=1

    return answer


# #############################################################

skill = "CBD"
skill_trees = ["BACDE", "CBADF", "AECB", "BDA"]
print(solution(skill, skill_trees))
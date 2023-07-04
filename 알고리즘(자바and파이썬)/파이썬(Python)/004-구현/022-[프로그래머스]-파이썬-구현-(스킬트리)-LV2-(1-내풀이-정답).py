# [프로그래머스]-파이썬-구현-(스킬트리)-LV2-(1-내풀이-정답).py
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

* 설계 [총 10분 소요] / 총 풀이 시간[총 21분 소요]
> skill에 대해서 문자열 리스트(list_skill)로 푼다. >>> list_skill = list(skill)
> list_skill의 각 원소를 dic_skill(딕셔너리)의 키로 지정하고,
각 키마다 val을 더해준다. (val은 1부터 시작 && 1씩 증가)
> for문을 활용
- skill_trees의 각 인덱스에 대해서 문자열 리스트(list_tree)로 푼다.
    - cnt = 0 / flag = True로 초기화
        - list_tree에 있는 각 값이 딕셔너리 키에 없는 거면 pass
        - list_tree에 있는 것이라면
            - cnt 값 1 더함
            - dic_skill[list_tree의 값]과 cnt 값 비교
                - 만약 같다면 계속 진행 / 다르다면 flag는 False && break
                - 끝까지 하고나서 flag가 그대로 True라면 answer값 1 증가

'''
#===================================================================================

def solution(skill, skill_trees):
    answer = 0

    list_skill = list(skill)
    dic_skill = dict()
    val = 1
    for i in range(len(list_skill)):
        dic_skill[list_skill[i]] = val
        val += 1

    for i in range(len(skill_trees)):
        list_tress = list(skill_trees[i])
        cnt = 0; flag = True

        for j in range(len(list_tress)):
            if dic_skill.get(list_tress[j]) == None:
                continue

            else:
                cnt += 1

                if dic_skill[list_tress[j]] == cnt:
                    continue

                else:
                    flag = False
                    break

        if flag == True:
            answer += 1

    return answer


# #############################################################

skill = "CBD"
skill_trees = ["BACDE", "CBADF", "AECB", "BDA"]
print(solution(skill, skill_trees))
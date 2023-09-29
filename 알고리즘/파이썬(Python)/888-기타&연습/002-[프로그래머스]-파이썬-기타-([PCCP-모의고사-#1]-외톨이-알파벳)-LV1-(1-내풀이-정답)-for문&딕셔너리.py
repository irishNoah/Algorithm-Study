# [프로그래머스]-파이썬-기타-([PCCP-모의고사-#1]-외톨이-알파벳)-LV1-(1-내풀이-정답)-for문&딕셔너리.py
# https://github.com/irishNoah/Algorithm-Study
# https://school.programmers.co.kr/learn/courses/15008/lessons/121683

'''
*** 제한 > 시간 : ?초 (기본 1초) / 메모리 : ?MB (기본 128MB)

*** 조건(제한사항)


*** 설계 [총 10분 소요] / 총 풀이 시간[총 25분 소요]
> for문을 활용
    이전 값과 다른 경우에만 cmp 문자열에 더한다.
> cmp에 있는 것을 딕셔너리
> cmp[소문자] 값이 2이상인 것만 리스트에 할당
> 리스트 정렬 answer 출력

*** 정확성 테스트
- 100점
'''
# #############################################################

import sys

def solution(input_string):

    input_string = "A" + input_string

    cmp = ""
    for i in range(1, len(input_string)):
        if input_string[i] != input_string[i-1]:
            cmp += input_string[i]

    cnt = dict() # 제발 괄호 좀 하자!!!!!
    answer = ""
    for word in cmp:
        if cnt.get(word) == None:
            cnt[word] = 1
        else:
            cnt[word] += 1

            if cnt[word] == 2:
                answer += word
            else:
                continue

    if answer == "":
        return "N"
    else:
        return "".join(sorted(answer))

# =========================================================


input_string = "zbzbz"
print(solution(input_string))


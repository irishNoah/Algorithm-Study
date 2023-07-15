# [프로그래머스]-파이썬-완전탐색-(모의고사)-LV1-(1-내풀이-성공).py
# https://github.com/irishNoah/Algorithm-Study
# https://school.programmers.co.kr/learn/courses/30/lessons/42840

'''
*** 참고 URL


*** 시간 : 2초 (기본 1초) / 메모리 : 128MB (기본 128MB)

*** 조건

*** 설계 [18분 소요] / 총 풀이 시간[총 25분 소요]
>> 수포자1, 2, 3을 > pA, pB, pC로 지정
>> 주어진 answer와 pA(길이 5), pB(길이 8), pC(길이 10)가 얼마나 일치하는가를 확인하려면?
    - 예를 들어 answer과 pA로 본다면?
        - answer[i] == pA[i % 5] 가 참이면 cntA의 값을 1 더해주면 됨
            - pB와 pC도 이와 동일한 원리!!!
>> cntA, cntB, cntC의 max값 체크
- 예제 2처럼, A나 B나 C의 값이 모두 동일하고, 따라서 최대값이 같은 상황
- 그렇기 때문에, 우선, cntA, cntB, cntC에서 max 값을 구하고
max값이 cntA, cntB, cntC와 일치하면 [1,2,3] 중에서 어팬드
- 이후 오름차순 정렬 후 리턴
'''
# #############################################################

import sys

def solution(answers):
    answer = []

    pA = [1,2,3,4,5] # 길이 5
    pB = [2,1,2,3,2,4,2,5] # 길이 8
    pC = [3,3,1,1,2,2,4,4,5,5] # 길이 10

    cntA = 0; cntB = 0; cntC = 0
    for i in range(len(answers)):
        if answers[i] == pA[i%5]:
            cntA += 1
        if answers[i] == pB[i%8]:
            cntB += 1
        if answers[i] == pC[i%10]:
            cntC += 1

    maxVal = max(cntA, cntB, cntC)
    if maxVal == cntA:
        answer.append(1)
    if maxVal == cntB:
        answer.append(2)
    if maxVal == cntC:
        answer.append(3)

    return answer


# =========================================================

answers = [1,3,2,4,2]
print(solution(answers)) # [1,2,3]
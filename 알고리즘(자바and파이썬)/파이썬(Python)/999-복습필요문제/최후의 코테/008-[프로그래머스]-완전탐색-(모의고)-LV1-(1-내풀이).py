'''
008-[프로그래머스]-완전탐색-(모의고)-LV1-(1-내풀이).py

- https://school.programmers.co.kr/learn/courses/30/lessons/42840?language=python3
- 16분 컷
'''

def solution(answers):
    ans = []
    
    # 각 수포자가 번호를 찍는 방식
    pA = [1,2,3,4,5] # 5개
    pB = [2,1,2,3,2,4,2,5] # 8개
    pC = [3,3,1,1,2,2,4,4,5,5] # 10개
    
    # 각 수포자가 찍어서 맞힌 개수에 대한 변수
    cntA = 0; cntB = 0; cntC = 0
    
    for i in range(len(answers)):
        if answers[i] == pA[i % len(pA)]:
            cntA += 1
        if answers[i] == pB[i % len(pB)]:
            cntB += 1
        if answers[i] == pC[i % len(pC)]:
            cntC += 1
    
    # 가장 많이 맞춘 사람의 개수를 maxVal에 담는다.
    maxVal = max(cntA, max(cntB, cntC))
    
    # 가장 높은 점수를 받은 사람이 여럿일 경우, return하는 값을 오름차순 정렬하기 위해
    # 차례대로 maxVal하고 비교해서 ans 리스트에 append해준다.
    if maxVal == cntA:
        ans.append(1)
    if maxVal == cntB:
        ans.append(2)
    if maxVal == cntC:
        ans.append(3)
    
    return ans
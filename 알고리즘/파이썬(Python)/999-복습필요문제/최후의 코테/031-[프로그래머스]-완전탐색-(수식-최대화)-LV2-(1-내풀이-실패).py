'''
031-[프로그래머스]-완전탐색-(수식-최대화)-LV2-(1-내풀이-실패).py
* 15:45 ~ 16:30 >>> 45분 / 못풀음 

### 주소
> https://school.programmers.co.kr/learn/courses/30/lessons/67257

### 참고
> 없음

### 설계 분, 총 분
1. 주어진 expression에 대해 for에 idx 기준으로 접근하여
isdigit()을 통해서, 숫자와 수식을 구분한다.
2. 있는 수식을 기준으로 수식 우선순위를 구한다.
3. 수식 우선순위에 따라 계산을 진행하여, result 리스트에 할당한다.
    - 구해진 계산이 음수일 경우에는, abs()를 통해 절댓값으로 변환한 것으로
    result에 할당한다.
4. result의 최댓값을 return한다.

'''

from itertools import permutations
from collections import deque

def solution(expression):
    answer = 0
    
    s = list(expression)
    arr = [] # 수와 계산 기호를 구분
    digit = "" # 수 구하기
    code = [] # 계산 수식
    
    for idx in range(len(expression)):
        if s[idx].isdigit() == True:
            digit += s[idx]
            
            # 마지막 수 뒤에는 계산 수식이 없으므로 
            # 마지막 수는 여기서 할당
            if idx == len(expression)-1:
                    arr.append(digit)   
                    break
        else:
            arr.append(digit)   # 구한 수 할당
            digit = ""          # digit 초기화
            arr.append(s[idx])  # 계산 기호 할당
            
            if s[idx] not in code:
                code.append(s[idx])
    
    # 계산 수식 우선순위 정하기
    rank = list(map(list, permutations(code, len(code))))
    # print("rank = ", rank)

    ### 수식을 계산한다.
    result = []
    arr = deque(arr)
    dq = deque()
    
    ############################ 여기서부터 못풀음 ㅠㅠㅠㅠㅠ
    for cmp in rank: # 계산 수식 우선순위(rank) 기준으로 계산을 돈다.
        copy = arr
        for idx in range(len(cmp)):
            if cmp[idx] == copy
    
    return answer
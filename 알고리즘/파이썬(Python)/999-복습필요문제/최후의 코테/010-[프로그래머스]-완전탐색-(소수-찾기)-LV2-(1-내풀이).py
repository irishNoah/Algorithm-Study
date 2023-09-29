'''
010-[프로그래머스]-완전탐색-(소수-찾기)-LV2-(1-내풀이).py

### 주소
> https://school.programmers.co.kr/learn/courses/30/lessons/42839

### 설계 7분, 총 29분
> 순열은 r개를 택할 때 순서대로 택하는 것
> 조합은 순서와 관계없이 그냥 택하는 것
> 순열 및 조합 안에 들어가는 인자들의 순서 파악하기
> 에라토스테네스의 소수 기억 해놓기
'''

from itertools import permutations

def solution(numbers):
    cnt = 0 # 소수 개수
    
    numbers = list(numbers)
    arr = []
    
    # 순열 이용
    for i in range(1, len(numbers)+1):
        for per in permutations(numbers, i):
            val = int("".join(per))
            
            if val not in [0, 1]:
                arr.append(val)
    

    arr = list(set(arr)) # 중복 수 제거
    
    # 에라토스테네스의 체
    for val in arr:
        flag = True # 아래 for문이 끝났을 때도 flag가 True이어야만 소수에 해당
        for i in range(2, int(val ** 0.5)+1): # 제곱근으로 소수 판별
            if val % i == 0:
                flag = False
                break
        
        if flag == True: # 소수일 경우 cnt 증가
            cnt += 1
    
    return cnt
'''
038-[프로그래머스]-카카오-복습필요(k진수에서-소수-개수-구하기)-LV2-(1-내풀이).py

### 주소
> https://school.programmers.co.kr/learn/courses/30/lessons/92335

### 참고
> 다른 사람의 풀이

15:40~:16:14
### 설계 5분, 총 34분
>

'''

import math

### 에라토스테네스의 체
def isPrime(val):
    val = int(val)
    for idx in range(2, int(val**0.5)+1):
        if val % idx == 0:
            return False
        
    return True

def solution(n, k):
    
    # 소수 구하기
    cng = ""
    while n != 0:
        mok = n // k
        rest = n % k
        cng += str(rest)
        n = n // k
    cng = cng[::-1]

    ### cng 리스트 변환
    arr = list(cng.split("0"))
    
    ### 소수 판별
    answer = 0
    for val in arr:
        if val == "1" or val == "": # cng 리스트에 ""가 있을 수도 있음에 유의
            continue
        
        if isPrime(val) == True:
            answer += 1        
    
    return answer
'''
034-[프로그래머스]-자료구조-(주식가격)-LV2-(2-다른풀이).py

### 주소
> https://school.programmers.co.kr/learn/courses/30/lessons/42584

### 참고
> https://velog.io/@soo5717/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EC%A3%BC%EC%8B%9D%EA%B0%80%EA%B2%A9-Python

23:18~23:45
### 설계 13분, 총 27분


'''

from collections import deque

def solution(prices):
    dq = deque(prices)
    
    answer = []
    
    while dq:
        cmp = dq.popleft()
    
        sec = 0
        for val in dq:
            sec += 1
            if val < cmp:
                break
        
        answer.append(sec)
    
    return answer
    
    
    
    
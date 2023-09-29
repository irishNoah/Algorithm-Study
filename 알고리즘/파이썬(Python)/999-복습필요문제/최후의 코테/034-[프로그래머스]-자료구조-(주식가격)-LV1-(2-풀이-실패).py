'''
034-[프로그래머스]-자료구조-(주식가격)-LV1-(1-풀이-실패).py

### 주소
> https://school.programmers.co.kr/learn/courses/30/lessons/42584

### 참고
> 없음

23:18~23:45
### 설계 13분, 총 27분
1. arr = prices[::-1] >>> 스택 활용하려고
- idx = 0
2. while True
> cmp = arr.pop()
    - 기준 가격
> 만약, idx가 len(prices)-1과 동일할 경우
    - answer에 0을 할당하고 while문 break
> seek = prices[idx+1:]
    - 슬라이싱
> for - seek를 돌아
    - cmt += 1
    - 만약, seek의 값이 cmp보다 작아져?
        - answer에 cnt 할당
        - break

'''

def solution(prices):
    answer = []
    arr = prices[::-1]
    idx = -1
    
    while True:
        idx += 1
        if idx == len(prices)-1:
            answer.append(0); break
        
        cmp = arr.pop()
        seek = prices[idx+1:]
        
        cnt = 0
        for val in seek:
            cnt += 1
            if val < cmp:
                break
        answer.append(cnt)
        
        
    return answer






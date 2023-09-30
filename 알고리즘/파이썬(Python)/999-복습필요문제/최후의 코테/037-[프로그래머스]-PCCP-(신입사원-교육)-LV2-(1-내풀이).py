'''
037-[프로그래머스]-PCCP-(신입사원-교육)-LV2-(1-내풀이).py

### 주소
> https://school.programmers.co.kr/learn/courses/15009/lessons/121688

### 참고
> 다른 사람의 풀이

00:30~00:47
### 설계 6분, 총 17분
> 최소 힙 자료구조를 사용

'''

import heapq

def solution(ability, number):
    answer = 0
    
    heapq.heapify(ability) # 최소힙 구성
    
    while number != 0:
        number -= 1
        
        val1 = heapq.heappop(ability)
        val2 = heapq.heappop(ability)
        
        hap = val1 + val2
        heapq.heappush(ability, hap)
        heapq.heappush(ability, hap)
    
    arr = list(ability)
    return sum(arr)
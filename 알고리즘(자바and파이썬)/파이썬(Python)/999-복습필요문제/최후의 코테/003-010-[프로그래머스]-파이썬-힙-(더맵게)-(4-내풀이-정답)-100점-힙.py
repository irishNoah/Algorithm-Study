# [프로그래머스]-파이썬-힙-(더맵게)-(4-내풀이-정답)-100점-힙.py
# https://github.com/irishNoah/Algorithm-Study

'''
*** 제한 > 시간 : 10초 (기본 1초) / 메모리 : 2GB (기본 128MB)

*** 조건

*** 설계 [총 -분 소요] / 총 풀이 시간[총 31분 소요]
- 전체적인 소스코드는 맞았는데, heappop()과 heappush()를 써야 하는 것을
- pop()과 push() 로 사용하였음

*** 참고
-

'''
#===================================================================================
import heapq

def solution(scoville, K):
    answer = 0
    
    heapq.heapify(scoville) # 최소힙 생성
    
    while scoville[0] < K: # 최상단 원소(즉, 최소값)가 스코빌 지수 이상이 될 때까지
        # 계속 섞어서 음식이 1개 밖에 안남았음에도
        # 이 음식의 스코빌 지수가 K 미만이면 -1 리턴
        if len(scoville) == 1:
            if scoville[0] < K:
                answer = -1
                break
        
        val1 = heapq.heappop(scoville)
        val2 = heapq.heappop(scoville)
        
        mix = val1 + (2*val2)
        heapq.heappush(scoville, mix)
        answer += 1
    
    return answer

#===================================================================================

# 예제 1
scoville = [1,2,3,9,10,12]
K = 7
print(solution(scoville, K)) # 2

# def solution(scoville, K):
#     answer = 0
#     return answer
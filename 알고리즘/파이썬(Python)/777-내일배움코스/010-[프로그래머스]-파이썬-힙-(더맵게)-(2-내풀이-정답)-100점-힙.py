# [프로그래머스]-파이썬-힙-(더맵게)-(2-내풀이-정답)-100점-힙.py
# https://github.com/irishNoah/Algorithm-Study

'''
*** 제한 > 시간 : 10초 (기본 1초) / 메모리 : 2GB (기본 128MB)

*** 조건

*** 설계 [총 -분 소요] / 총 풀이 시간[총 -분 소요]
- 힙을 활용해서 했다.
- 힙 삽입 & 삭제 (O(log N))

*** 참고
> 파이썬 힙 기초
- https://littlefoxdiary.tistory.com/3
- https://www.daleseo.com/python-heapq/

'''
#===================================================================================
import heapq

def solution(scoville, K):
    answer = 0

    # 최소 힙 구현하기
    '''
    heap1 모듈은 최소 힙 기능만을 동작하므로, 
    최대 힙 활용은 약간의 요령이 필요
    '''
    heapq.heapify(scoville) # O(N)

    while scoville[0] < K:
        # 애초부터 길이가 1이었거나, 계속 섞어서 길이가 1이 됐을 때(즉, 음식이 하나 남았을 때)
        # 이 값이 스코빌 지수 K보다 작다면 -1 리턴
        if len(scoville) == 1:
            if scoville[0] < K:
                answer = -1
                break

        # 가장 안 매운 음식과, 두번째 안매음 음식 pop
        min1 = heapq.heappop(scoville) # O(log(n))
        min2 = heapq.heappop(scoville) # O(log(n))

        val = min1 + (2 * min2) # 섞어
        # 섞은거 넣어줘 > 이 때 자기의 값에 맞는 자리로 찾아간다.
        heapq.heappush(scoville, val) # O(log(n))
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
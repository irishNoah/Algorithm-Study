# [프로그래머스]-파이썬-힙-(더맵게)-(3-강사풀이-정답)-100점-힙.py
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

    heapq.heapify(scoville)
    while True:
        min1 = heapq.heappop(scoville)
        if min1 >= K:
            break
        elif len(scoville) == 0:
            answer = -1
            break

        min2 = heapq.heappop(scoville)
        new_scoville = min1 + 2*min2
        heapq.heappush(scoville, new_scoville)
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
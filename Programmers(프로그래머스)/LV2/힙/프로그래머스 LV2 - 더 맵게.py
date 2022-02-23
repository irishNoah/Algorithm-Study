# 프로그래머스 LV2 - 더 맵게
# https://programmers.co.kr/learn/courses/30/lessons/42626

# 정확성 테스트의 케이스 16개 중 16개 성공
# 효율성 테스트의 케이스 5개 중 5개 성공
# 총점 100.0점

import heapq

def solution(scoville, K):
    answer = 0 # 리턴할 값 answer

    '''
    scoville 오름차순 정렬하기.
    이렇게 하는 이유는 힙은 최소 또는 최대값만 찾아서 알려줄 뿐, 정렬이 되지 않은 상황 때문임.
    밑에 있는 while문에 scoville[0] < K 조건이 있는데, 
    scoville[0]이 K 이하라면 더 이상 비교할 필요가 없기 때문에
    이를 위해 정렬을 해준 것임,
    '''
    scoville.sort() 

    while scoville[0] < K:
        '''
        문제 조건 중
        "모든 음식의 스코빌 지수를 K 이상으로 만들 수 없는 경우에는 -1을 return 합니다."이
        있으므로 아래 if문 실행. 만약 scoville의 길이가 1 이하가 아닐 경우 그 밑에 else문 수행
        '''
        if len(scoville) <= 1:
            return -1


        else:
            # 가장 맵지 않은 음식의 스코빌 지수를 small에 대입
            small = heapq.heappop(scoville)

            # 두 번째로 맵지 않은 음식의 스코빌 지수를 small에 대입
            small2 = heapq.heappop(scoville)

            # 섞은 음식의 스코빌 지수를 scoville에 삽입
            heapq.heappush(scoville, (small + (small2 * 2)))

            # 리턴값 answer은 1 증가시키기
            answer += 1

    return answer

scoville = [1, 2, 3, 9, 10, 12]
K = 7
print(solution(scoville, K)) # 출력 결과 예 : 2
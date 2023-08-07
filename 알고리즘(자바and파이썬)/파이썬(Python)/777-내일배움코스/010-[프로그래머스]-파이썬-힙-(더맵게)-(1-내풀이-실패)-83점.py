# [프로그래머스]-파이썬-힙-(더맵게)-(1-내풀이-정확성통과효율성실패)-83점.py
# https://github.com/irishNoah/Algorithm-Study

'''
*** 제한 > 시간 : 10초 (기본 1초) / 메모리 : 2GB (기본 128MB)

*** 조건

*** 설계 [총 -분 소요] / 총 풀이 시간[총 -분 소요]
- 2 <= 스코빌 리스트 길이 <= 백만
    - O(log N) 이하의 시간 복잡도

*** 참고
- answer > 섞은 횟수
    - 처음에 0으로 초기화
- 처음부터 모든 스코빌 지수가 K 이상이면 계산할 필요가 없음
    - 바로 answer 리턴
- 스코빌에서 최소값을 찾는다.
    - 만약, 최소값이 K이상이면 모든 것이 K 이상이기 때문에 answer을 리턴
    - 최소값이 K 미만이면
        - 최소값을 val1에 할당
        - val1의 인덱스 찾기
        - del을 통해서 최소값 제거
        - 그 다음 최소값을 찾는다.
        - 이거는 val2에 할당
        - val2의 인덱스 찾기
        - del을 통해서 두 번째 최소값 제거
        - mix = val1 + (2 * val2)
        - 이 mix 값을 스코빌에 append


'''
#===================================================================================

def solution(scoville, K):
    answer = 0
    # print(min(scoville))

    # 처음부터 스코빌의 모든 지수가 K 이상이면 계산할 필요가 없음
    if min(scoville) >= K:
        return answer

    while min(scoville) < K: # 기존에 <= 로 기호를 했는데, 이것 때문에 정확성 테스트 3개 틀림
        # 만약 끝까지 믹스해서 음식이 1개 밖에 안남은 상태에서
        # 이 음식의 스코빌 지수가 K보다 작을 경우 -1 리턴
        if len(scoville) == 1 and min(scoville) < K:
            return -1

        # 만약 끝까지 믹스해서 음식이 1개 밖에 안남은 상태에서
        # 이 음식의 스코빌 지수가 마침 k와 같다면 answer 리턴
        if len(scoville) == 1 and min(scoville) == K:
            break

        # 나머지 경우
        val1 = min(scoville)
        idx1 = scoville.index(val1)
        del(scoville[idx1])

        val2 = min(scoville)
        idx2 = scoville.index(val2)
        del(scoville[idx2])

        print("del scoville = ", scoville)

        mix = val1 + (2 * val2)
        scoville.append(mix)
        print("new scoville = ", scoville)

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
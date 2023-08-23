# [백준]15649-(N과M(1))-(백트레킹)-S3-(2-참고)-그래프+백트래킹.py
# https://github.com/irishNoah/Algorithm-Study
# https://www.acmicpc.net/problem/15649

'''
*** 제한 > 시간 : ?초 (기본 1초) / 메모리 : ?MB (기본 128MB)

*** 조건

*** 설계 [총 -분 소요] / 총 풀이 시간[총 -분 소요]
- 코드 참고

*** 참고
> https://veggie-garden.tistory.com/24

'''
#===================================================================================

import sys
input = sys.stdin.readline

N, M = map(int, input().split())

result = [] # 수열 리스트
def back(): ### 재귀 함수
    # 재귀 조건 >>> 수열 리스트의 길이가 M가 같을 때
    if len(result) == M:
        print(*result)
        return

    for node in range(1, N+1): ### 수열 생성
        ### 중복되는 수열이 있으면 안되므로, 리스트에 있는지 체크
        if node not in result:
            result.append(node) # 없는 경우에만 수열 리스트에 추가
            back() # 재귀 함수 수행
            result.pop() # 재귀 함수 복귀 지점

back()

#===================================================================================
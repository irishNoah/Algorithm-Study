# [백준]15650-(N과M(2))-(백트레킹)-S3-(1-내풀이-정답)-백트래킹+정렬.py
# https://github.com/irishNoah/Algorithm-Study
# https://www.acmicpc.net/problem/15650

'''
*** 제한 > 시간 : 1초 (기본 1초) / 메모리 : 256MB (기본 128MB)

*** 조건

*** 설계 [총 -분 소요] / 총 풀이 시간[총 15분 소요]
>>> 116ms 소요

*** 참고

'''
#===================================================================================
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

result = [] # 수열 리스트
def back(): ### 재귀 함수 구현

    if len(result) == M: # 재귀 조건
        cmp = sorted(result)

        ### result와 오름차순 정렬된 result가 같을 경우에만 출력
        if result == cmp:
            print(*result)
        return

    for node in range(1, N+1):
        if node not in result:
            result.append(node)
            back()
            result.pop()

back()





#===================================================================================
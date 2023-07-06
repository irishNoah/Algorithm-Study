# [백준]1748-구현-(수-이어-쓰기-1)-S4-(1-내풀이-실패)-시간초과.py
# https://github.com/irishNoah/Algorithm-Study
# https://www.acmicpc.net/problem/1748

'''
*** 시간 : 0.5초 (기본 1초) / 메모리 : 128MB (기본 128MB)


*** 조건
- N(1 ≤ N ≤ 100,000,000)

*** 설계 [총 2분 소요] / 총 풀이 시간[총 5분 소요]
- 다 문자열 ans에 더해준 다음에 ans의 길이를 구한다.

*** 결과
- 시간초과

'''
#============================================================

import sys

input = sys.stdin.readline().rstrip

n = int(input())

ans = ""
for val in range(1, n+1):
    ans += str(val)

print(len(ans))
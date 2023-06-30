# [백준]17484-완전탐색-(진우의-달-여행-(Small))-S3-(2-다른풀이-참고-이해안감).py
# https://github.com/irishNoah/Algorithm-Study
# https://www.acmicpc.net/problem/17484

'''
* 제한 > 시간 : 1초 (기본 1초) / 메모리 : 256MB (기본 128MB)
- 제한시간 1초
- N(가로), M(세로)의 범위 >>> N, M (2≤ N, M ≤ 6)
- 각 행렬의 원소값 <= 100

>>> 제한 시간은 1초이지만 메모리가 256MB인점 그리고 데이터 개수 및 범위를 봤을 때
탐색일 가능성이 높다.

>>> 또한, 이 문제 특성상 dp일 가능성도 있다.

* 설계 [총 -분 소요] / 총 풀이 시간[총 -분 소요]

* 다른 점
> 이해가 잘 가지 않는다. >>> for문에서
> dp = [[[0,0,0] for _ in range(M)]] + [[[float('inf'),float('inf'),float('inf')] for _ in range(M)] for _ in range(N)]
- 범위 flow를 방지하고자 이렇게 구현한 것 같은데, 이 점은 배워야 겠다.


'''
#============================================================

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
dp = [[[0,0,0] for _ in range(M)]] + [[[float('inf'),float('inf'),float('inf')] for _ in range(M)] for _ in range(N)]

for i in range(1,N+1):
    for j in range(M):
        if j < M-1:
            dp[i][j][0] = min(dp[i-1][j+1][1],dp[i-1][j+1][2]) + matrix[i-1][j]
        if 0 < j:
            dp[i][j][2] = min(dp[i-1][j-1][1],dp[i-1][j-1][0]) + matrix[i-1][j]
            
        dp[i][j][1] = min(dp[i-1][j][0],dp[i-1][j][2]) + matrix[i-1][j]

min_value = float('inf')
for row in dp[i]:
    for each in row:
        min_value = min(min_value,each)

print(dp)
print(min_value)
# [백준]2167-구현-(2차원-배열의-합)-S5-(1-참고)-DP활용.py
# https://github.com/irishNoah/Algorithm-Study
# https://www.acmicpc.net/problem/2167

'''
*** 참고 URL
코드 > https://velog.io/@norighthere/%EB%B0%B1%EC%A4%80-2167-2%EC%B0%A8%EC%9B%90-%EB%B0%B0%EC%97%B4%EC%9D%98-%ED%95%A9
설명 > https://ssafy-story.tistory.com/74

*** 시간 : 2초 (기본 1초) / 메모리 : 128MB (기본 128MB)

*** 조건

*** 설계 [8분 소요] / 총 풀이 시간[총 20분 소요]

'''
#============================================================

# 배열의 크기 입력
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

# 부분의 개수 입력
K = int(input())
dp = [[0] * (M+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, M+1):
        dp[i][j] = arr[i-1][j-1] + dp[i][j-1] + dp[i-1][j] - dp[i-1][j-1]

for _ in range(K):
    i, j, x, y = map(int, input().split())
    print(dp[x][y] - dp[x][j-1] - dp[i-1][y] + dp[i-1][j-1])
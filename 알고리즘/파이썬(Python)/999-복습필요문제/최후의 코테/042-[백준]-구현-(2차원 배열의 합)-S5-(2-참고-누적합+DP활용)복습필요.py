'''
042-[백준]-구현-(2차원 배열의 합)-S5-(2-참고-누적합+DP활용)복습필요.py

### 주소
> https://www.acmicpc.net/problem/2167

### 참고
> https://ssafy-story.tistory.com/74

13:55 ~ 14:27
### 설계 10분, 총 32분


'''
#===================================================================================

# 누적합 풀이
n, m = map(int, input().split())
lst = []
dp = [[0]*(m+1) for _ in range(n+1)]

for _ in range(n):
    lst.append(list(map(int, input().split())))

for i in range(1, n+1):
    for j in range(1, m+1):
        # dp[i-1][j-1]은 dp[i][j-1]과 dp[i-1][j]의 누적합을 구할 때 사용됐으므로
        # 2번 더해지므로, 한번 빼준다. (본래값 + 왼쪽 + 위쪽 - 대각선)
        dp[i][j] = lst[i-1][j-1] + dp[i][j-1] + dp[i-1][j] - dp[i-1][j-1]

k = int(input())
for _ in range(k):
    i, j, x, y = map(int, input().split())
    # dp[x][j-1]과 dp[i-1][y]에서 겹치는 부분 dp[i-1][j-1] 더해주기
    print(dp[x][y] - dp[x][j-1] - dp[i-1][y] + dp[i-1][j-1])


#===================================================================================
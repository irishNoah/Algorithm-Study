# [백준]1904번-동적계획법-(01타일)-S3-(3-복습)
# https://github.com/irishNoah/Algorithm-Study
# https://www.acmicpc.net/problem/1904

n = int(input())

if n == 1 or n == 2:
    print(n)
    exit()

dp = [0] * (n+1)

dp[1] = 1; dp[2] = 2

for i in range(3, n+1):
    dp[i] = (dp[i-1] + dp[i-2]) % 15746

print(dp[n])
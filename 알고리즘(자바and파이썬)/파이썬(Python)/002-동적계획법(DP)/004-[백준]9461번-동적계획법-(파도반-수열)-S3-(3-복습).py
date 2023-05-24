# [백준]9461번-동적계획법-(파도반-수열)-S3-(3-복습)
# https://github.com/irishNoah/Algorithm-Study
# https://www.acmicpc.net/problem/9461

n = int(input())

cnt = 0

dp = [0] * 101
dp[1] = 1; dp[2] = 1; dp[3] = 1

while True:
    cnt += 1
    long = int(input())

    if 1 <= long <= 3:
        print(dp[long])
        continue

    for i in range(4, long+1):
        dp[i] = dp[i-2] + dp[i-3]

    print(dp[long])

    if cnt == n:
        break
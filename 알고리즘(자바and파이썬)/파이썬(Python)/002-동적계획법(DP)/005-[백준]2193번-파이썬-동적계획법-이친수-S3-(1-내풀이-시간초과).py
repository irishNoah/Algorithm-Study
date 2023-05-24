# [백준]2193번-파이썬-동적계획법-이친수-S3-(1-내풀이).py
# https://github.com/irishNoah/Algorithm-Study
# https://www.acmicpc.net/problem/2193

'''
이렇게 풀어도, IDE 상에서는 정답을 도출해낼 수 있었다.
하지만, 백준에서는 시간 초과 판정이 났다.
n의 수가 작으면 모르겠지만, n의 범위가 90이므로
이진수로 이루어진 90자리 수에 대해서 for문으로 일일이
조건을 따진다면, 시간 초과가 날 수밖에 없을 것이다.

해당 문제는 DP를 활용해야 한다.
'''

n = int(input())

start = pow(2, n-1)
last = pow(2, n)

cnt = 0

# 이친수 구하기
for value in range(start, last):
    seek = bin(value)[2:]

    if "11" not in seek:
        cnt += 1

print(cnt)
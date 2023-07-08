# [백준]2167-구현-(2차원-배열의-합)-S5-(1-내풀이-시간초과)-for문활용.py
# https://github.com/irishNoah/Algorithm-Study
# https://www.acmicpc.net/problem/2167

'''
*** 참고 URL

*** 시간 : 2초 (기본 1초) / 메모리 : 128MB (기본 128MB)

*** 조건


*** 설계 [8분 소요] / 총 풀이 시간[총 20분 소요]

'''
#============================================================

import sys

N, M = map(int, sys.stdin.readline().rstrip().split())

arr = [list(map(int, input().split())) for _ in range(N)]

K = int(input())
infor = [list(map(int, input().split())) for _ in range(K)]

for a in range(len(infor)):
    answer = 0
    i, j, x, y = infor[a][0], infor[a][1], infor[a][2], infor[a][3]

    #1 > i = x, j = y
    if i == x and j == y:
        answer = arr[i-1][j-1]

    #2 > i = x, j != y
    elif i == x and j != y:
        for b in range(j-1, y):
            answer += arr[i-1][b]

    # 3 > i != x, j == y
    elif i != x and j == y:
        for b in range(i-1, x):
            answer += arr[b][j-1]

    # 4 > i != x, j != y
    else:
        for b in range(i - 1, x):
            for c in range(j - 1, y):
                answer += arr[b][c]

    print(answer)

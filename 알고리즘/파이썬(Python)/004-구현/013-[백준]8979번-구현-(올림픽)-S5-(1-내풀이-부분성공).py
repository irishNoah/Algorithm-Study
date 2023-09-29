# [백준]8979번-구현-(올림픽)-S5-(1-내풀이-부분성공).py
# https://github.com/irishNoah/Algorithm-Study
# https://www.acmicpc.net/problem/8979

'''
# 문제 풀이

@ 람다 정렬 참고 > https://haesoo9410.tistory.com/193
@ 내 풀이 > 8점

'''

import sys

n, k = map(int, sys.stdin.readline().split())

info = []
for _ in range(n):
    arr = list(map(int, sys.stdin.readline().split()))
    info.append(arr)


# 금-은-동 순으로 정렬
info.sort(key=lambda x: (x[1], x[2], x[3]), reverse=True)



rank = 1

if k == info[0][0]:
    print(rank)

else:
    for i in range(1, n):
        if k == info[i][0]:
            print(rank)
            break

        if (info[i - 1][1] == info[i][1]) and (info[i - 1][2] == info[i][2]) and (info[i - 1][3] == info[i][3]):
            continue

        rank += 1
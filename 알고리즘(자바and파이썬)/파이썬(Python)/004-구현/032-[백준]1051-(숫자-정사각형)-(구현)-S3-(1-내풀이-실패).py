# [백준]1051-(숫자-정사각형)-(구현)-S3-(1-내풀이-실패).py
# https://github.com/irishNoah/Algorithm-Study
# https://www.acmicpc.net/problem/1051

'''
*** 제한 > 시간 : 2초 (기본 1초) / 메모리 : 128MB (기본 128MB)

*** 조건

*** 설계 [총 22분 소요] / 총 풀이 시간[총 39분 소요]

*** 참고

'''
#===================================================================================

import sys
input = sys.stdin.readline

a, b = map(int, input().split())

k = min(a, b)

graph = []
for _ in range(a):
    graph.append(list(map(int, input().rstrip())))

result = 0
flag = False
while True:
    for i in range(0, b-(k-1)):
        for j in range(i, i+k):

            p1 = graph[i][j]
            p2 = graph[i][j+(k-1)]
            p3 = graph[i+(k-1)][j]
            p4 = graph[i+(k-1)][j+(k-1)]

            print(p1, p2, p3, p4)

            if p1 == p2 == p3 == p4:
                flag = True
                break

    if flag == True:
        break

    k = k-1

print(k*k)


#===================================================================================
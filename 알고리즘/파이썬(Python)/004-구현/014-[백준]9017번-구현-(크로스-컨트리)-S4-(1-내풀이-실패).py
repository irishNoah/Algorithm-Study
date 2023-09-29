# [백준]9017번-구현-(크로스-컨트리)-S4-(1-내풀이-실패).py
# https://github.com/irishNoah/Algorithm-Study
# https://www.acmicpc.net/problem/9017

'''
# 문제 풀이

1. 각 등수에 대한 점수 매기기 (팀 인원수가 6인 팀만 해당)까지는 잘 구한 것 같은데...
2. 우승팀 구하기에서 문제를 맞이하였다 ㅎㅎ
3. 검색해도 잘 안나온다.... 확실히 푼 사람이 적어서 그런감?

'''

import sys

T = int(sys.stdin.readline())

while True:
    T = T-1

    n = int(sys.stdin.readline())

    arr = list(map(int, sys.stdin.readline().split()))

    max = max(arr); hap = 99999
    winner = 0

    # 각 등수에 대한 점수 매기기 (팀 인원수가 6인 팀만 해당)
    # 6인 미만은 0으로 세팅
    cnt = 1
    point = []
    for i in range(0, len(arr)):
        if arr.count(arr[i]) == 6:
            point.append(cnt)
            cnt += 1

        else:
            point.append(0)


# =============================================================

    # 우승팀 구하기
    for i in range(1, max+1):
        rank = 0

        if arr.count(i) == 6:

            idx = [j for j, ele in enumerate(arr) if ele == i]

            check = 0
            for k in idx:
                check += 1

                rank += point[k]

                if check == 4:
                    break


        if rank <= hap:
            hap = rank
            winner = i


    print(winner)


    if T == 0:
        break
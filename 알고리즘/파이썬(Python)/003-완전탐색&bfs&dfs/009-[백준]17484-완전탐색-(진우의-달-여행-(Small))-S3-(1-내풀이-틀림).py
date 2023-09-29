# [백준]17484-완전탐색-(진우의-달-여행-(Small))-S3-(1-내풀이-틀림).py
# https://github.com/irishNoah/Algorithm-Study
# https://www.acmicpc.net/problem/17484

'''
* 제한 > 시간 : 1초 (기본 1초) / 메모리 : 256MB (기본 128MB)
- 제한시간 1초
- N(가로), M(세로)의 범위 >>> N, M (2≤ N, M ≤ 6)
- 각 행렬의 원소값 <= 100

>>> 제한 시간은 1초이지만 메모리가 256MB인점 그리고 데이터 개수 및 범위를 봤을 때
탐색일 가능성이 높다.

* 설계 [총 18분 소요] / 총 풀이 시간[총 70분 소요]
> N(가로), M(세로)를 입력 받는다.
> 리스트 arr을 생성
> for문으로 N에 맞게 route 리스트에 할당
- route를 arr에 할당

> for문으로 최소값 비교
# 세로[0번째] & 세로[마지막 번째]인 경우에는
- 세로[0번째] >>> 제일 좌측이므로 flag = -1
- 세로[마지막 번째] >>> 제일 우측이므로 flag = 1
- 나머지는? >>> flag = 0
# 방향
- 왼쪽 선택 : move = left >>> 다음 방향은 왼쪽 불가
- 오른쪽 선택 : move = right >>> 다음 방향은 오른쪽 불가
- 가운데 선택 : move = middle >>> 다음 방향은 가운데 불가
>>> 맨 처음 행은 move = middle 이라고 한다.

# 전략
- 이전 방향 값과 flag를 확인해서 각 선택할 수 있는 최선의 경우를 구한다.

* 왜 틀렸을까?
- print()문으로 111~999 해본 결과 res가 resulut에 할당이 안됨....


'''
#============================================================

import sys

N, M = map(int, sys.stdin.readline().rstrip().split())

arr = []
for _ in range(N):
    value = list(map(int, sys.stdin.readline().rstrip().split()))
    arr.append(value)

print(arr)

before_move = "middel" # 우주선 방향
garo = 0 # 행 인덱스
res = 0 # 최소값
result = []

for j in range(M): # 세로로 간다
    print("111")
    if garo == 0:
        res += arr[garo][j]
        print(res)

        if j == 0:
            # flag >>> 세로의 위치 판단 (맨 왼쪽 : -1 / 맨 우측 : 1 / 나머지 : 0)
            flag = -1
        if j == M-1:
            flag = 1
        else:
            flag = 0

        garo += 1
        continue
    print("222")

    # 세로 위치 판단
    if j == 0: # 맨 왼쪽
        flag = -1
    elif j == M-1: # 맨 오른쪽
        flag = 1
    elif j != 0 and j != M-1: # 중간 어딘가
        flag = 0
    print("333")

    print("444")
    # 이전 방향 값 토대로 이번 방향 값 정하기 및 계산
    if before_move == "middel":
        if flag == -1: # 오른쪽 이동만 가능
            before_move == "right"
            res += arr[garo][j+1]

        elif flag == 1: # 왼쪽 이동만 가능
            before_move == "left"
            res += arr[garo][j - 1]

        else: # flag == 0 # 왼쪽 및 오른쪽 이동만 가능
            check = min(arr[garo][j - 1], arr[garo][j + 1])

            if check == arr[garo][j - 1]:
                before_move == "left"
            else:
                before_move == "right"

            res += check

        print(res)
        garo += 1
    print("555")

    print("666")
    if before_move == "left":
        if flag == -1: # 가운데 또는 오른쪽 이동만 가능
            check = min(arr[garo][j], arr[garo][j + 1])

            if check == arr[garo][j]:
                before_move == "middle"
            else:
                before_move == "right"

            res += check

        elif flag == 1: # 가운데 또는 왼쪽 이동만 가능
            check = min(arr[garo][j], arr[garo][j - 1])

            if check == arr[garo][j]:
                before_move == "middle"
            else:
                before_move == "left"

            res += check

        print(res)
        garo += 1

    print("777")
    if before_move == "right":
        if flag == 1:  # 가운데 또는 왼쪽 이동만 가능
            check = min(arr[garo][j], arr[garo][j - 1])

            if check == arr[garo][j]:
                before_move == "middle"
            else:
                before_move == "left"

            res += check

        elif flag == 0: # 가운데 또는 왼쪽 이동만 가능
            check = min(arr[garo][j], arr[garo][j - 1])

            if check == arr[garo][j]:
                before_move == "middle"
            else:
                before_move == "left"

            res += check

        print(res)
        garo += 1
    print("888")

    print("999")
    if garo == N+1:
        print(res)
        result.append(res)
        res = 0
        garo == 0

print(result)
print(min(result))
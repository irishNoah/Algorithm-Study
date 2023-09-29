# [백준]1018-완전탐색-(체스판-다시-칠하기)-S4-(1-내풀이-일부만정답).py
# https://github.com/irishNoah/Algorithm-Study
# https://www.acmicpc.net/problem/1018

'''
* 제한 > 시간 : 2초 / 메모리 : 128MB
- 제한시간 2초
- N(가로), M(세로)의 범위 >>> 8 <= N & M <= 50

* 설계 [총 15분 소요] / 총 풀이 시간[총 48분 소요]
> 가로(garo)와 세로(sero) 입력
> 타일 입력 - 2차원 리스트(arr)에 할당
> 2차원 for문 활용
- 각 범위 내에 있는 B와 W개수 파악
- B와 W의 차이의 철댓값 구해서 차이값 리스트(brick)에 할당
> brick의 최소값 구하기
> 최소값 //2 를 출력

* 틀린 이유
- 2차원 for문의 가로 및 세로 설정 범위에서 틀렸다.

'''
#============================================================

import sys

garo, sero = map(int, sys.stdin.readline().split())

arr = []
for _ in range(garo):
    tile = list(sys.stdin.readline().rstrip())
    arr.append(tile)

'''
가로값이 10일 경우 2차원 리스트에서는
가로를 0~7 / 1~8 / 2~9 번째 비교를 해야 한다.
따라서, 가로의 타일 비교 범위를 구해주고, point로 체크한다.

세로 역시 위와 동일한 원리이다.
'''
limit_garo = garo-8
point_garo = -1

limit_sero = sero-8
point_sero = -1


brick = []

while True:
    point_garo = point_garo + 1

    # while문 탈출
    if point_garo > limit_garo:
        break

    cntB = 0; cntW = 0;

    for i in range(point_garo, point_garo+8):
        point_sero = point_sero +1

        if point_sero > limit_sero:
            point_sero = -1
            continue

        for j in range(point_sero, point_sero+8):
            if arr[i][j] == 'B':
                cntB += 1
            elif arr[i][j] == 'W':
                cntW += 1

    minusBW = abs(cntB-cntW)
    brick.append(minusBW)

res = min(brick) // 2
print(res)
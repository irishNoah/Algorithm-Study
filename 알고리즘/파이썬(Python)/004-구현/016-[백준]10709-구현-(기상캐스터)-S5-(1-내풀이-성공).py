# [백준]10709-구현-(기상캐스터)-S5-(1-내풀이-성공).py
# https://github.com/irishNoah/Algorithm-Study
# https://www.acmicpc.net/problem/10709

'''
# 문제 풀이
> h,w 때문에 2차원 for문을 활용할 수도 있는 문제였으나
실제 각 행의 기상 여부는 다음 행에 상관 없으니
각 행으로만 접근해서 풀면 되므로 1차원 for문만 활용 


'''
import sys

h, w = map(int, sys.stdin.readline().split())

result = []

while True:
    h = h-1

    arr = list(map(str, sys.stdin.readline()))
    cast = []

    if arr[0] == 'c':
        cast.append(0)

    elif arr[0] == '.':
        cast.append(-1)

    cnt = 1 # cnt > 분이라고 생각하면 됨

    for i in range(1, w):
        # 기존에 구름이 좌표에 있었을 경우
        if arr[i] == 'c':
            cast.append(0)
            cnt = 1

        # 기존 좌표가 . 이었으나 앞에 있는 좌표 중 구름이 있었을 경우 > 분 계산
        if arr[i] == '.' and cast[i-1] != -1:
            cast.append(cnt)
            cnt += 1

        # 기존 좌표가 . 이었으나 앞에 있는 좌표 중 구름이 없는 경우 > -1
        if arr[i] == '.' and cast[i-1] == -1:
            cast.append(-1)

    result.append(cast)

    if h == 0:
        break

for j in range(len(result)):
    print(*(result[j]))
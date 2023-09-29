# [백준]20006-구현-(랭킹전-대기열)-S2-(2-참고-정답).py
# https://github.com/irishNoah/Algorithm-Study
# https://www.acmicpc.net/problem/20006

'''
# 문제 풀이

1. 내 풀이와 다른 점 > flag

'''
import sys

P, M = map(int, sys.stdin.readline().split())
rooms = []

# 각각의 플레이어를 입력 받아 방에 넣어주기
for p in range(P):
    l, n = map(str, sys.stdin.readline().split())
    # 최초 입력된 플레이어
    if not rooms:
        rooms.append([[int(l), n]])
        continue

    # 방에 들어갔는지 확인 하는 flag변수
    enter = False
    # 각 방을 돌면서
    for room in rooms:
        # 조건에 합당하면 넣어주기
        if len(room) < M and room[0][0] - 10 <= int(l) <= room[0][0] + 10:
            room.append([int(l), n])
            enter = True
            break
    # 못들어갔으면 새로운 방을 파서 넣어주기
    if not enter:
        rooms.append([[int(l), n]])

# 이름 기준 정렬
for room in rooms:
    room.sort(key=lambda x: x[1])

# 정원 수에 따라 출력
for room in rooms:
    if len(room) == M:
        print('Started!')
    else:
        print('Waiting!')
    for lv, name in room:
        print(lv, name)
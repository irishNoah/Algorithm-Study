# [백준]20006-구현-(랭킹전-대기열)-S2-(1-내풀이-부분성공).py
# https://github.com/irishNoah/Algorithm-Study
# https://www.acmicpc.net/problem/20006

'''
# 문제 풀이

1. 예제에서 Started까지는 잘 한 것 같은데, 어느 부분에서 끊겼는지 모르겠당

'''

import sys

p, m = map(int, sys.stdin.readline().split())

check = p
player = []
while True:
    check = check-1

    l, n = map(str, sys.stdin.readline().split())
    l = int(l)

    # player[?][0] > 레벨 / player[?][0] > 닉네임
    player.append([l, n])

    if check == 0:
        break

room = []
room.append([player[0]])
#------------------------------------------------------

for i in range(1, p):
    for j in range(len(room)):
        if len(room[j]) < m:
            # 기존 생성 방들의 첫 번째 플레이어와 비교해서, 비교 플레이어의 레빌이 +- 10 사이에 있을 때
            if room[j][0][0]-10 <= player[i][0] <= room[j][0][0]+10 :
                room[j].append(player[i])
                break

            # 레벨 범위 값을 넘어갈 경우 새로운 방 생성
            else:
                room.append([player[i]])
                break

        elif len(room[j]) == m:
            room.append([player[i]])
            break

    if i == p-1:
        break

print(room)

for k in range(len(room)):
    if len(room[k]) == m:
        print("Strated!")
        for y in range(len(room[k])):
            print(room[k][y])

    else:
        print("Waiting!!")
        for y in range(len(room[k])):
            print(room[k][y])
# [백준]2979-구현-(트럭-주차)-B2-(3-복습-성공).py
# https://github.com/irishNoah/Algorithm-Study
# https://www.acmicpc.net/problem/2979

'''
# 문제 풀이

1. 시작 시간~종료 시간에 대해 리스트에 할당할 때
일반적으로 아는 timing 범위로 넣으면 안된다.
2. count() 메소드를 쓸 것이라면 굳이 정렬을 할 필요가 없다.

'''
#============================================================

import sys

a, b, c = map(int, sys.stdin.readline().split())

arr = []
for _ in range(3):
    start, finish = map(int, sys.stdin.readline().split())

    # 이 부분을 주의하자
    for i in range(start+1, finish+1):
        arr.append(i)

res = 0

for j in arr:
    if arr.count(j) == 1:
        res += a
    elif arr.count(j) == 2:
        res += b
    elif arr.count(j) == 3:
        res += c

print(res)
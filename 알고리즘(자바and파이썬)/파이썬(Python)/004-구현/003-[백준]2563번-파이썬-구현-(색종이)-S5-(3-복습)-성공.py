# [백준]2563번-파이썬-구현-(색종이)-S5-(3-복습)-성공.py
# https://github.com/irishNoah/Algorithm-Study
# https://www.acmicpc.net/problem/2563

'''

'''

n = int(input())

cnt = 0

table = [[0]*100 for _ in range(100)]

while True:
    cnt += 1
    a, b = map(int, input().split())

    for i in range(a, a+10):
        for j in range(b, b+10):
            table[i][j] = 1

    if cnt == n:
        break

check = 0
for i in range(0, 100):
    for j in range(0, 100):
        if table[i][j] == 1:
            check += 1

print(check)
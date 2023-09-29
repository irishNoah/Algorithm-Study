# [백준]11047번-그리디-동전0-S4
# https://github.com/irishNoah/Algorithm-Study
# https://www.acmicpc.net/problem/11047

n, k = map(int, input().split())

money = []

for _ in range(n):
    value = int(input())

    money.append(value)

money.reverse()

cnt = 0 # 동전 개수

while True:

    for i in range(0, n):
        if k == 0:
            break

        if k // money[i] > 0:
            cnt += k // money[i]

            k = k - (money[i] * (k // money[i]))

    break

print(cnt)
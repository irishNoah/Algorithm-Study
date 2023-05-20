# [백준]2720번-그리디-(세탁소사장동혁)-B3-3(복습)
# https://github.com/irishNoah/Algorithm-Study
# https://www.acmicpc.net/problem/2720

n = int(input())

for _ in range(n):
    coin = int(input())

    for money in [25, 10, 5, 1]:
        mok = coin // money

        coin -= money * mok

        print(mok, end=" ")

    print()


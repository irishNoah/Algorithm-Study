# [백준]2960-파이썬-구현-(에라토스테네스의 체)-S4-(2-참고)-.py
# https://github.com/irishNoah/Algorithm-Study
# https://www.acmicpc.net/problem/2960

'''
# 느낀점

> n의 최대 약수가 sqrt(n) 이하이므로 i=sqrt(n)까지 검사만 하는 것이 핵심 포인트이다.
'''

N, K = map(int, input().split())
tmp = 0
sieve = [True] * (N + 1)

for i in range(2, N + 1):
    # i의 배수만 확인하면 되므로 step = i로 하면 된다.
    for j in range(i, N + 1, i):
        if sieve[j] != False:
            sieve[j] = False
            tmp += 1
            if tmp == K:
                print(j)
                break

    if tmp == K:
        break
# [백준]1292번-구현-(쉽게푸는문제)-B1-(1-내풀이-성공).py
# https://github.com/irishNoah/Algorithm-Study
# https://www.acmicpc.net/problem/1292

'''
# 문제 풀이

1. 배열 규칙을 보면 각 수에 해당되는 것만큼 리스트에 할당됨
> x = [k] * k

2. extend() 메소드를 사용해 리스트에 추가

'''

import sys

def sol(a,b):

    arr = []
    k = 1; check = b

    while True:
        x = [k] * k
        arr.extend(x)

        check = check - k
        k = k+1

        if check <= k:
            x = [k] * check
            arr.extend(x)

            break

    answer = sum(arr[a-1:b])
    return  answer

a, b = map(int, sys.stdin.readline().split())
print(sol(a,b))
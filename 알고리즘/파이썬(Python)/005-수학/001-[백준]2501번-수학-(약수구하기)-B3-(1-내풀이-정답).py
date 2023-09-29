# [백준]2501번-수학-(약수구하기)-B3-(1-내풀이-정답).py
# https://github.com/irishNoah/Algorithm-Study
# https://www.acmicpc.net/problem/2501

'''
# 문제 풀이
- for문을 구해서 약수를 구한다.
- 약수에 해당하면 k를 1 차감한다.
- k가 0이 되면 for문 탈출

'''

import sys

def sol(n, k):
    cnt = 0
    answer = 0

    for i in range(1, n+1):
        if n % i == 0:
            k = k-1

        if k == 0:
            answer = i
            break

    return answer


n, k = map(int, sys.stdin.readline().split())
print(sol(n,k))
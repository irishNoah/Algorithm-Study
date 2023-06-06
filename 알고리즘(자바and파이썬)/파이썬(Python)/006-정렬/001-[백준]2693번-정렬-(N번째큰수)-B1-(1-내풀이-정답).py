# [백준]2693번-정렬-(N번째큰수)-B1-(1-내풀이-정답).py
# https://github.com/irishNoah/Algorithm-Study
# https://www.acmicpc.net/problem/2693

'''
# 문제 풀이

1. 오름차순 정렬
2. 뒤에서 3번째꺼 출력

'''

import sys

def sol(test):

    while True:
        test = test-1

        arr = []
        arr = list(map(int, sys.stdin.readline().split()))

        arr = sorted(arr)

        print(arr[-3])

        if test == 0:
            break


test = int(sys.stdin.readline())
sol(test)
# [백준]3460번-구현-(이진수)-B3-(1-내풀이-성공).py
# https://github.com/irishNoah/Algorithm-Study
# https://www.acmicpc.net/problem/3460

'''
# 문제 풀이

1. 입력된 10진수를 이진수로 변환 - 단, 슬라이싱을 활용해 '0b' 생략

'''

import sys

def sol(test):
    while True:
        num = int(sys.stdin.readline())

        # bin()은 앞에 '0b'표시가 있어서 슬라이싱을 활용해 이진수 자체만 보관
        cvt = bin(num)[2:]

        digit = 0

        for i in range(len(cvt)-1, -1, -1):
            if cvt[i] == "1":
                print(digit, end=" ")

            digit = digit+1

        test = test - 1

        if test == 0:
            break

test = int(sys.stdin.readline())
sol(test)
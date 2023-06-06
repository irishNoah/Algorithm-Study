# [백준]10818번-구현-(최소최대)-B3-(1-내풀이-성공).py
# https://github.com/irishNoah/Algorithm-Study
# https://www.acmicpc.net/problem/10818

'''
# 문제 풀이

1. 리스트에서 max()와 min() 활용해 최대값, 최소값 구함

'''

import sys

def sol(n):

    arr = list(map(int, sys.stdin.readline().split()))

    print("%d %d"%(min(arr), max(arr)))

n = int(sys.stdin.readline())
sol(n)
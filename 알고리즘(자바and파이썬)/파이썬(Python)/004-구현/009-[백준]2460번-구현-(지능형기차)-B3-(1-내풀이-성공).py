# [백준]2460번-구현-(지능형기차)-B3-(1-내풀이-성공).py
# https://github.com/irishNoah/Algorithm-Study
# https://www.acmicpc.net/problem/2460

'''
# 문제 풀이

1. 각 역마다의 결과(hap) = 이전 역 결과(hap) - 내린 사람(a) + 탄 사람(b)
2. 새로운 역의 결과가 이전의 최대 결과보다 크면 answer에 할당

'''

import sys

hap = 0
answer = 0

for i in range(0, 10):
    a, b = map(int, sys.stdin.readline().split())

    hap = hap-a+b

    if answer <= hap:
        answer = hap

print(answer)